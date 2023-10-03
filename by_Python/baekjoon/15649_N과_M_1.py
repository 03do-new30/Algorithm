import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def solve(seq, visited):
    if len(seq) == m:
        print(' '.join(list(map(str, seq))))
        return

    for i in range(1, n+1):
        if not visited[i]:
            new_seq = seq + [i]
            visited[i] = True
            solve(new_seq, visited)
            visited[i] = False


for i in range(1, n+1):
    v = [False] * (n+1)
    v[i] = True
    solve([i], v)
