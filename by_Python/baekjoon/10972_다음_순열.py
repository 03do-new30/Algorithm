# 출처: https://jshong1125.tistory.com/14
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

# 뒤에서부터 수를 비교
find = False
for i in range(N-1, 0, -1):
    # i번째 값이 (i-1)번째 값보다 클 때
    if seq[i-1] < seq[i]:
        for j in range(N-1, 0, -1):
            # (i-1)번째 값보다 큰 값을 가지는 seq[j]를 찾는다.
            if seq[i-1] < seq[j]:
                seq[i-1], seq[j] = seq[j], seq[i-1] # swap
                seq = seq[:i] + sorted(seq[i:]) # i 이상의 인덱스를 갖고 있는 숫자들 처리해주기
                find = True
                break
    
    if find:
        print(' '.join(map(str, seq)))
        break

if not find:
    print(-1)
