import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

# 각 숫자 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지
# 상한과 하한을 이분탐색을 이용하여 구현

# lower bound
def lower_bound(target):
    left = 0
    right = n-1
    position = -1

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            position = mid # 하한은 target보다 작거나 같은 수 중 첫번째 수
            # 하한을 찾기 위해 더 왼쪽을 바라봄
            right = mid - 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return position

# upper bound
def upper_bound(target):
    left = 0
    right = n-1
    position = -1

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            position = mid + 1 # 상한은 target보다 큰 수 중 첫번쨰 수
            # 상한을 찾기 위해 더 오른쪽을 바라봄
            left = mid + 1
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return position

arr.sort()
# print("arr:", arr)
answer = []
for num in nums:
    lower = lower_bound(num)
    upper = upper_bound(num)
    # print("target number:", num, "-> lower:", lower, ", upper:", upper)
    cnt = upper - lower
    answer.append(cnt)

print(' '.join(map(str, answer)))