import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 1
right = max(arr) # 설정할 수 있는 길이의 최대값

while left <= right:
    # mid 길이로 설정하고 나무를 자를 떄
    mid = (left + right) // 2
    cnt = 0
    for tree in arr:
        if tree <= mid:
            continue
        cnt += (tree - mid)
    # print("cnt:", cnt)
    if cnt < m:
        # 높이를 더 낮게 설정해야 함
        right = mid - 1
    else:
        # 높이를 더 높게 설정해야 함
        left = mid + 1

# print("left:", left, "mid:", mid, "right:", right)
print(right)