import sys
input = sys.stdin.readline
from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

cmds = ['*', '+', '-', '/']

visited = dict()
visited[s] = ''
q = deque([s])
while q:
    s = q.popleft()
    if s == t:
        break
    for cmd in cmds:
        if cmd == '*':
            next = s * s
        elif cmd == '+':
            next = s + s
        elif cmd == '-':
            next = s - s
        else:
            if s == 0:
                continue
            next = s // s
        if 1 <= next <= 10**9:
            if next not in visited:
                visited[next] = visited[s] + cmd
                q.append(next)
if t not in visited:
    print(-1)
else:
    print(visited[t])