import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 구간 합 이용
prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

# 구간 합 출력
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])