import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
n = len(nums)

seq = [0] * m
def solve(idx, selected):
    if selected == m:
        print(' '.join(list(map(str, seq))))
        return
    
    for i in range(idx, n):
        seq[selected] = nums[i]
        solve(i, selected + 1)

solve(0, 0)
