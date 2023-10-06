import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

# 이전 순열
# 주어진 순열이 어떤 숫자들로 시작하는 순열의 첫번째 순열인지 판별
# 그 이전 순열은 또 다른 어떤 숫자들로 시작하는 순열의 마지막 순열

### 1 ###
# seq[i-1] > seq[i]인 가장 큰 i를 찾는다
for i in range(n-1, -1, -1):
    if i == 0:
        print(-1)
        break
    
    if seq[i-1] > seq[i]:
        ### 2 ###
        # seq[i-1]보다 작은 seq[j] (i <= j < n) 중 가장 큰 seq[j] 를 찾아 swap
        for j in range(n-1, i-1, -1):
            if seq[i-1] > seq[j]:
                seq[i-1], seq[j] = seq[j], seq[i-1]
                break
        ### 3 ###
        # 이전 순열은 seq[:i] + reversed(seq[i:])
        seq = seq[:i] + list(reversed(seq[i:]))

        print(' '.join(list(map(str, seq))))
        break