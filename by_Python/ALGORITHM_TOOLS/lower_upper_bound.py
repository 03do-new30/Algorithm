arr = [10, 9, 2, 3, 4, 1, 7, 17, 18, 130]
arr.sort() # 정렬 필수
n = len(arr)

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