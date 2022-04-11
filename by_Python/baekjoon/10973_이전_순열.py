# 출처: https://ji-gwang.tistory.com/264
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if seq[i-1] > seq[i]:
        for j in range(N-1, 0, -1):
            if seq[i-1] > seq[j]:
                seq[i-1], seq[j] = seq[j], seq[i-1]
                seq = seq[:i] + sorted(seq[i:], reverse=True)
                print(*seq)
                exit()

print(-1)
