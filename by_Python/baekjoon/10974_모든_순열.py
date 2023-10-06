import sys
input = sys.stdin.readline

n = int(input())

seq = [0] * n
visited = [False] * (n+1)
def solve(idx):
    if idx == n:
        print(' '.join(list(map(str, seq))))
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        seq[idx] = i
        solve(idx + 1)
        visited[i] = False

solve(0)