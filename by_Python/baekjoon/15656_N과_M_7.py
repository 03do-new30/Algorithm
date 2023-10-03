import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = [0] * m

def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return
    
    for num in nums:
        seq[idx] = num
        solve(idx + 1)

solve(0)