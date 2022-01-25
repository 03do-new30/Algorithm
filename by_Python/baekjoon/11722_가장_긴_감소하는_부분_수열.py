import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))

# 가장 긴 감소하는 부분 수열 =
# 수열을 거꾸로한 것의 최장 증가 부분 수열을 구한 것
a.reverse()
# dp[x] = 길이가 x인 증가하는 부분수열 중 마지막 숫자의 최소값 저장
dp = [0]
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        if a[i] in dp:
            continue
        for j in range(1, len(dp)):
            if dp[j] > a[i]:
                dp[j] = a[i]
                break

print(len(dp)-1)
