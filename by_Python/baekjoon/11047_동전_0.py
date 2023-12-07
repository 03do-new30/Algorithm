import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 동전의 가치, a[i]는 a[i-1]의 배수 -> 그리디 알고리즘
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
for i in range(-1, -len(a) -1, -1):
    if k <= 0:
        break
    ans += k // a[i]
    k = k % a[i]
print(ans)