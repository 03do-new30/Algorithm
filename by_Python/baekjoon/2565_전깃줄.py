import sys
input = sys.stdin.readline

n = int(input().strip())
# A[i] = 전봇대 A의 위치 i에 연결된 전봇대 B의 위치 정보
# A[i] == 0이면 연결되지 않은 것을 의미
A = [0]*(501)
for _ in range(n):
    a, b = map(int, input().split())
    A[a] = b


# 전깃줄이 교차하지 않으려면 A[i]에 연결된 B의 위치 정보가 A[i+1]에 연결된 B의 위치 정보보다 반드시 작아야 한다.
# A를 수열로 보고, LIS로 만들어본다.
# dp[x] = 증가하는 부분수열의 길이가 x일 때, 마지막 숫자의 최소값을 저장
# 이 때, dp[x]의 값이 "교체" 될 때, 교차하지 않게 하기 위해 없앤 것으로 본다.
dp = [0]
count = 0  # 제거한 전선 개수
for i in range(1, 501):
    if A[i] == 0:
        continue  # skip

    if dp[-1] < A[i]:
        dp.append(A[i])
    elif dp[-1] > A[i]:
        # 교체
        for j in range(1, len(dp)):
            if A[i] < dp[j]:
                dp[j] = A[i]
                count += 1  # 교체 = 제거 횟수 증가
                break
print(count)
