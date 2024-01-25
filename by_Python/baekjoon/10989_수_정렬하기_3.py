import sys
input = sys.stdin.readline

n = int(input())
# cnt[i] = 숫자 i의 등장 횟수
cnt = [0] * 10001
for _ in range(n):
    cnt[int(input())] += 1

for i in range(len(cnt)):
    if cnt[i] > 0:
        for j in range(cnt[i]):
            print(i)