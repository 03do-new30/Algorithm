import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

# 그래프
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 공장이 위치한 섬의 번호
start, end = map(int, input().split())

# mid 중량으로 옮길 수 있는지 확인한다
def possible(island, mid, visited):
    if visited[island]:
        return False
    visited[island] = True
    if island == end:
        return True
    for other, weight in graph[island]:
        # other 다리를 건널 떄 중량제한이 현재 mid보다 크다면 옮길 수 있음
        if weight >= mid:
            # 확인해보기
            if possible(other, mid, visited):
                return True
    return False

left = 1 # 중량 최소
right = 1000000000 # 중량 최대
ans = 0
while left <= right:
    mid = (left + right) // 2
    # 섬 방문 표시
    visited = [False] * (n+1)
    if possible(start, mid, visited):
        # 옮길 수 있다면, 중량을 조금 더 늘려본다
        ans = mid
        left = mid + 1
    else:
        # 옮길 수 없다면, 중량을 줄여본다
        right = mid - 1

print(ans)