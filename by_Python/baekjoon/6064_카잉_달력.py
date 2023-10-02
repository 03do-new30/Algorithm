import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):

    m, n, x, y = map(int, input().split())

    x -= 1 # 나머지 연산 쉽게 하기 위해
    y -= 1 # 나머지 연산 쉽게 하기 위해

    k = x
    while k < n * m:
        if k % n == y:
            print(k + 1)
            break
        k += m
    else:
        print(-1)
