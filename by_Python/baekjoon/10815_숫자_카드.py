import sys
input = sys.stdin.readline

def binary_search(li, target):
    start = 0
    end = len(li) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if target == li[mid]:
            return True
        
        if target < li[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))
answer = []
for num in nums:
    if binary_search(cards, num):
        answer.append('1')
    else:
        answer.append('0')

print(' '.join(answer))