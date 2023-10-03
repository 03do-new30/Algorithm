import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n+1)  # 방문 여부 저장
seq = [-1] * m  # 수열 저장


def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return

    for num in range(1, n+1):
        if visited[num]:
            continue
        if (idx > 0 and seq[idx - 1] < num) or (idx == 0):
            visited[num] = True
            seq[idx] = num
            solve(idx + 1)
            visited[num] = False


solve(0)
