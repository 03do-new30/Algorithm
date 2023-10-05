import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

# 사전순으로 가장 앞서는 순열은 오름차순,
# 마지막에 오는 순열은 내림차순

### 1 ###
# seq[i-1] < seq[i]를 만족하는 가장 큰 i를 찾는다
# -> seq[:i]로 시작하는 순열 중 가장 마지막 순열이라고 할 수 있음
for i in range(n-1, -1, -1):
    if i == 0:
        print(-1)
        break

    if seq[i-1] < seq[i]:
        ### 2 ### 
        # seq[i-1] < seq[j]를 만족하는 가장 작은 seq[j]를 찾고, 위치를 바꾼다 (i <= j < n)
        swap_idx = -1
        for j in range(i, n):
            if seq[i-1] < seq[j]:
                swap_idx = j
        seq[i-1], seq[swap_idx] = seq[swap_idx], seq[i-1] # swap
        ### 3 ###
        # seq[:i] + reversed(seq[i:])를 하면 seq[:i]로 시작하는 순열중 가장 첫번째 순열이 완성된다
        answer = seq[:i] + list(reversed(seq[i:]))
        print(' '.join(list(map(str, answer))))
        break