# 출처: https://jaimemin.tistory.com/582
import sys
input = sys.stdin.readline
from collections import deque

def bfs(N, K):
    visited = [False]*100001
    visited[N] = True
    q = deque([(N, 0)])

    # 찾을 수 있는 가장 빠른 시간
    min_time = float('inf')
    # 가장 빠른 시간으로 찾는 방법
    min_time_ways = 0

    while q:
        # q에서 꺼낼 때! 방문 표시를 해주는 것이 핵심이다
        x, time = q.popleft()
        visited[x] = True

        if x == K:
            if time < min_time:
                min_time = time
                min_time_ways = 1
            elif time == min_time:
                min_time_ways += 1
            continue
        
        if 0 <= x - 1 < 100001 and not visited[x-1]:
            q.append((x-1, time + 1))
        
        if 0 <= x + 1 < 100001 and not visited[x+1]:
            q.append((x+1, time + 1))
        
        if 0 <= x * 2 < 100001 and not visited[x*2]:
            q.append((x*2, time + 1))
    
    return min_time, min_time_ways



N, K = map(int, input().split())
min_time, min_time_ways = bfs(N, K)
print(min_time)
print(min_time_ways)