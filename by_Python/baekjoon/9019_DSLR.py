import sys
input = sys.stdin.readline
from collections import deque

def solve(a, b):
    hist = [None] * 10000
    hist[a] = ''
    q = deque([a])

    while q:
        n = q.popleft()

        # D
        d = (n * 2) % 10000
        if hist[d] is None:
            hist[d] = hist[n] + 'D'
            q.append(d)

        # S
        if n == 0:
            s = 9999
        else:
            s = n - 1
        if hist[s] is None:
            hist[s] = hist[n] + 'S'
            q.append(s)
        # L
        l = (n % 1000) * 10 + (n // 1000)
        if hist[l] is None:
            hist[l] = hist[n] + 'L'
            q.append(l)
        # R
        r = (n % 10) * 1000 + (n // 10)
        if hist[r] is None:
            hist[r] = hist[n] + 'R'
            q.append(r)
    
    return hist[b]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))
    


    