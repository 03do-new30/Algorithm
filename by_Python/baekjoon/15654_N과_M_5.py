import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

seq = [-1] * m
visited = [False] * n


def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        seq[idx] = nums[i]
        solve(idx + 1)
        visited[i] = False


solve(0)
