arr = [1, 9, 9, 7, 330, 100, 4, 5, 6, 2]
n = len(arr)
arr.sort() # 정렬되어 있어야 함

def binary_search(target):
    left = 0
    right = n-1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return -1