import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 숫자 mid가 몇번째 위치를 차지하는지 확인하면서 범위를 조정하는 이분탐색
left = 1
right = n * n
ans = 0

# 숫자 mid의 배열 B에서의 위치는
# mid보다 작은 숫자들의 개수로 결정된다
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, mid//i) # mid보다 작은 숫자들의 개수를 저장
    if cnt >= k:
        ans = mid
        right = mid - 1
    else:
        # mid보다 작거나 같은 숫자의 개수가 k개보다 작으면 안됨
        left = mid + 1 # 범위를 큰쪽으로 옮긴다

print(ans)