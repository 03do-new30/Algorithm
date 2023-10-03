import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = [-1] * m

# 고른 수열은 오름차순이어야 한다 = 숫자 M개를 고르는 경우
def solve(start_idx, selected):
    if selected == m:
        print(' '.join(list(map(str, seq))))
        return
    
    for idx in range(start_idx, n):
        seq[selected] = nums[idx]
        solve(idx + 1, selected + 1)

solve(0, 0)