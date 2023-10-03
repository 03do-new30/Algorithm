import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = [0] * m

def solve(start_idx, selected):
    if selected == m:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(start_idx, n):
        seq[selected] = nums[i]
        solve(i, selected + 1)

solve(0, 0)