import sys
input = sys.stdin.readline

n, m = map(int, input().split())

seq = [-1] * m  # 수열 저장


def solve(idx, start):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return

    for num in range(start, n+1):
        seq[idx] = num
        solve(idx + 1, num + 1)


solve(0, 1)
