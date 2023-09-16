import sys
input = sys.stdin.readline

t = int(input())
nums = []
for _ in range(t):
    nums.append(int(input()))

# dp[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수
length = max(nums)
dp = [0] * (length + 1)

for i in range(1, length + 1):
    if i == 1:
        dp[i] = 1
        continue
    if i == 2:
        dp[i] = 2
        continue
    if i == 3:
        dp[i] = 4
        continue
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

""" 
[!] i == 1, i == 2, i == 3 반복문으로 검사하기보다는
[!] 아래처럼 처리해주는 것도 똑똑한 방법
[!] 단, d[0]에 값을 설정해줘야 함

d[0] = 1
for i in range(1, 11):
    if i-1 >= 0:
        d[i] += d[i-1]
    if i-2 >= 0:
        d[i] += d[i-2]
    if i-3 >= 0:
        d[i] += d[i-3]
"""

for num in nums:
    print(dp[num])