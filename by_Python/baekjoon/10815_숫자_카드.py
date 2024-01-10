import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

def binary_search(target):
    left = 0
    right = n-1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return 1
        elif target < arr[mid]:
            right = mid - 1
        elif target > arr[mid]:
            left = mid + 1
    return 0

arr.sort()
answer = []
for num in nums:
    answer.append(binary_search(num))
print(' '.join(map(str, answer)))