import sys
input = sys.stdin.readline

n = int(input())

# 1 ~ 9 -> 한자리 (9가지 숫자)
# 10 ~ 99 -> 두자리 (90가지 숫자)
# 100 ~ 999 -> 세자리 (900가지 숫자)
# ...
# 10,000,000 ~ 99,999,999 -> 여덟자리 (90,000,000가지 숫자)
# 100,000,000 -> 아홉자리 (1가지 숫자)

ans = 0
start = 1
length = 1

while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    ans += (end - start + 1) * length
    start *= 10
    length += 1
print(ans)