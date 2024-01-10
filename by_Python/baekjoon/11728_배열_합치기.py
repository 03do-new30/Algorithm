import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * (n + m)
i = 0; j = 0; k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] <= b[j]):
        c[k] = a[i]
        k += 1
        i += 1
    else:
        c[k] = b[j]
        k += 1
        j += 1
print(' '.join(map(str, c)))