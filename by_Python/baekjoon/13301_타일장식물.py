import sys
input = sys.stdin.readline

n = int(input().strip())

# fibonacci
fib = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        fib[1] = 1
    else:
        fib[i] = fib[i-1] + fib[i-2]

# perimiter
peri = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if i == 1:
        peri[1] = 4
    else:
        peri[i] = peri[i-1] + 2 * fib[i]

print(peri[n])
