import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

# 모든 E, S, M에서 1을 빼면
# year % 15 == E
# year % 28 == S
# year % 19 == M
# 인 year를 찾는 문제가 된다
E -= 1
S -= 1
M -= 1

for year in range(7981):
    if year % 15 == E and year % 28 == S and year % 19 == M:
        print(year + 1)
        break