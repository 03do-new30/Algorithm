import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# palindrome[i][j] = nums[i:j+1]이 팰린드롬인지 여부 저장
palindrome = [[False] * n for _ in range(n)]

# 우하향 대각선(\)으로 순회 
for x in range(n):
    for i in range(n):
        j = i + x
        if j >= n:
            break
        
        if i == j:
            palindrome[i][j] = True
        elif i + 1 == j:
            palindrome[i][j] = nums[i] == nums[j]
        else:
            palindrome[i][j] = (nums[i] == nums[j]) and palindrome[i+1][j-1]

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    if palindrome[s][e]:
        print(1)
    else:
        print(0)