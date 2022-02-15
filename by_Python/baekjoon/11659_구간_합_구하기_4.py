import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
prefix_sum = [0]*(N+1)

# prefix_sum[i] = 1번째 숫자부터 i번째 숫자까지의 합을 저장
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]

for _ in range(M):
    # i번째 수부터 j번째 수까지의 합
    # = prefix_sum[j] - prefix_sum[i-1]
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
