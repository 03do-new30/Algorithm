import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([(N, str(N))])
    visited[N] = True

    while q:
        x, history = q.popleft()

        if x == 1:
            return history
        
        if x % 3 == 0 and not visited[x//3]:
            visited[x//3] = True
            q.append((x//3, history + " " + str(x//3)))
        
        if x % 2 == 0 and not visited[x//2]:
            visited[x//2] = True
            q.append((x//2, history + " " + str(x//2)))
        
        if x - 1 >= 1 and not visited[x-1]:
            visited[x-1] = True
            q.append((x-1, history + " " + str(x-1)))
    
        


N = int(input())
visited = [False]*1000001
result = bfs()
print(len(result.split()) - 1)
print(result)