import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x):
    global ans

    visited[x] = True
    cycle.append(x)  # 지금까지의 팀 구성
    pick = arr[x]

    if visited[pick]:  # 이미 방문 했는가?
        if pick in cycle:  # cycle 내에 있는가? => cycle
            idx = cycle.index(pick)
            ans += cycle[idx:]
        return
    else:
        dfs(pick)


T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    arr = [0] + list(map(int, input().split()))
    visited = [True] + [False]*n

    # 팀을 정하는 데 성공한 학생들
    ans = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - len(ans))
