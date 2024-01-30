import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

# 이분탐색해가면서 자르면 몇개 나오는지 탐색
left = 1
right = max(arr) 
# right -> 랜선 길이의 최대값

while left <= right:
    mid = (left + right) // 2
    result = 0
    for lan in arr:
        result += lan // mid
    # print("result:", result)
    if result < n:
        # 랜선을 더 작게 잘라야 한다
        right = mid - 1
    else:
        # 랜선을 더 크게 잘라야 한다
        left = mid + 1

# print("left:", left, "mid:", mid, "right:", right)
print(right)