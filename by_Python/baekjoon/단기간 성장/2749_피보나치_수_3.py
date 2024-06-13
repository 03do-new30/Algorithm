import sys
input = sys.stdin.readline

n = int(input())

# 파사노 주기 활용
# 피보나치 수를 어떤 수 k로 나눌 때, 나머지는 항상 주기를 갖게 된다

# 주기의 길이를 P라고 하면, N번째 피보나치 수를 K로 나눈 나머지는 
# N % P 번째 피보나치 수를 M으로 나눈 나머지와 같다

# 주기는 K = 10^x일 때, 항상 15 * 10 ^(x-1)이다.

# 피보나치 수를 10^6으로 나눈 나머지를 찾아야 한다
cycle = 15 * (10**5)

dp = [0] * cycle
dp[0] = 0
n = n % cycle
for i in range(1, n+1):
    if i == 1:
        dp[i] = 1
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % (10**6)

print(dp[n])