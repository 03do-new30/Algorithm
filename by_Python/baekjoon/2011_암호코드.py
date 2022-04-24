import sys
input = sys.stdin.readline

nums = [' '] + list(input().strip())
dp = [0]*len(nums)
dp[0] = 1

valid = True

for i in range(1, len(nums)):
    if i == 1:
        if nums[1] == '0':
            valid = False
            break
        else:
            dp[1] = 1
        continue

    if 10 <= int(nums[i-1] + nums[i]) <= 26:
        if nums[i] == '0':
            dp[i] = dp[i-2]
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000
    else:
        if nums[i] == '0':
            valid = False
            break
        else:
            dp[i] = dp[i-1]

if valid:
    print(dp[-1])
else:
    print(0)