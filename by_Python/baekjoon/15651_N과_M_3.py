import sys
input = sys.stdin.readline

n, m = map(int, input().split())

seq = [-1] * m  # 수열 저장


def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return

    for num in range(1, n+1):
        seq[idx] = num
        solve(idx + 1)


solve(0)
