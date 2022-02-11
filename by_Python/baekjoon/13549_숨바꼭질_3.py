import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1]*100001
visited[N] = 0

q = deque([N])
while q:
    x = q.popleft()

    if x == K:
        print(visited[x])
        break

    """
    반례: 1 2가 입력으로 주어졌을 때
    0이 출력되어야하는데,
    x*2일 때의 검사를 마지막으로 해주면
    visited[x+1]이 먼저 갱신되어서 답이 1로 나온다!
    x*2를 먼저 검사해준다.
    """
    if 0 <= x * 2 < 100001 and visited[x*2] == -1:
        visited[x*2] = visited[x]
        # 0 - 1 BFS
        # 가중치가 0인 것은 큐의 뒤가 아니라 앞에 넣는다
        q.appendleft(x*2)
    if 0 <= x - 1 < 100001 and visited[x-1] == -1:
        visited[x-1] = visited[x] + 1
        q.append(x-1)
    if 0 <= x + 1 < 100001 and visited[x+1] == -1:
        visited[x+1] = visited[x] + 1
        q.append(x+1)
