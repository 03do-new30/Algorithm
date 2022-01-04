import sys
input = sys.stdin.readline

n = int(input().strip())

# dp[i][j] = 수의 길이가 j일 때, 마지막 숫자가 i(0<=i<10)인 오르막 숫자의 개수
dp = [[0] * (n+1) for _ in range(10)]

for j in range(1, n+1):
    for i in range(10):
        # base case
        if j == 1:
            dp[i][1] = 1

        else:
            for x in range(0, i+1):
                dp[i][j] += dp[x][j-1]

# n열의 합을 출력한다
result = 0
for row in dp:
    result += row[n]
print(result % 10007)
