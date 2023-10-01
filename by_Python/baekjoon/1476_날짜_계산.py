import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

# 하나씩 해보기
cnt = 1
e = 1
s = 1
m = 1
while e != E or s != S or m != M:
    e += 1
    s += 1
    m += 1
    cnt += 1
    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19
print(cnt)