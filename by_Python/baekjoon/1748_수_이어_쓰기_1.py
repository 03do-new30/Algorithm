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
length = len(str(n))
for i in range(1, length + 1):
    if i == length:
        ans += (n - 10**(i-1) + 1) * length
        break

    ans += i * (10 ** i - 10 ** (i-1))

    # print("i:", i, "ans:", ans)

print(ans)