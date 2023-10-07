import sys
input = sys.stdin.readline

t = int(input())
nums = []
for _ in range(t):
    nums.append(int(input()))

def solve(sum, goal):
    if sum > goal:
        return 0
    
    if sum == goal:
        return 1
    
    ret = 0
    ret += solve(sum + 1, goal)
    ret += solve(sum + 2, goal)
    ret += solve(sum + 3, goal)
    return ret

for num in nums:
    print(solve(0, num))