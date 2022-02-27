import sys
input = sys.stdin.readline

n = int(input().strip())

# 자릿수
i = 0
tmp = n
while tmp > 0:
    tmp = tmp // 10
    i += 1

# 새로운 수의 자릿수 출력하기
ans = 0
for x in range(1, i+1):
    if x == i:
        ans += n * x
    else:
        ans += (10**x - 10**(x-1)) * x
        n -= (10**x - 10**(x-1))

print(ans)
