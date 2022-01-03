import sys
input = sys.stdin.readline

n = int(input().strip())

t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for i in range(1, n+1):
    time, price = map(int, input().split())
    t[i] = time
    p[i] = price

# Pn을 지급받을 수 있는 날은 그 날로부터 Tn일 뒤라고 생각하자
# dp[i] = 근무한지 i일째일 때, 얻을 수 있는 최대 수익
# 퇴사일인 n+1일까지 받을 수 있는 수익을 계산하기 위해서 dp 길이를 하나 더 길게 설정
dp = [0 for _ in range(n+2)]

# dp[i] = j + Tj <= i인것 중 max(dp[j] + Pj)
"""
d[j] + Pj
j일까지 받은 급여 + j일의 상담을 통해 받을 수 있는 급여
"""
for i in range(1, n+2):
    max_price = 0
    for j in range(1, i):
        if j + t[j] <= i:
            max_price = max(max_price, dp[j] + p[j])
    dp[i] = max_price

print(max(dp))
