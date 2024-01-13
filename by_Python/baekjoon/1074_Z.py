import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def power2(num):
    return 2**num

def solve(n, r, c):
    if n == 1:
        return r*2 + c
    
    if r < power2(n-1):
        # 왼쪽 상단
        if c < power2(n-1):
            return solve(n-1, r, c)
        # 오른쪽 상단
        else:
            return solve(n-1, r, c - power2(n-1)) + power2(2 * n - 2)
    else:
        # 왼쪽 하단
        if c < power2(n-1):
            return solve(n-1, r - power2(n-1), c) + power2(2 * n - 2) * 2
        # 오른쪽 하단
        else:
            return solve(n-1, r - power2(n - 1), c - power2(n - 1)) + power2(2 * n - 2) * 3

print(solve(n, r, c))