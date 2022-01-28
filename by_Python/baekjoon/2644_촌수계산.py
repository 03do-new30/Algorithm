from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
x, y = map(int, input().split())
m = int(input().strip())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    parent, child = map(int, input().split())
    # 양방향 그래프로 설정해준다
    graph[parent].append(child)
    graph[child].append(parent)

"""
for row in graph:
    print(row)
print('-'*30)
"""

# distance[v] = v까지의 거리
# -1 = 방문하지 않음
distance = [-1]*(n+1)


def bfs(node):
    # node와 연결된 모든 노드들의 거리를 구한다
    q = deque([])
    q.append(node)
    distance[node] = 0

    while q:
        node = q.popleft()
        for new_node in graph[node]:
            # 방문하지 않았다면
            if distance[new_node] == -1:
                q.append(new_node)
                # 이전 노드까지의 거리 + 1
                distance[new_node] = distance[node]+1


# 촌수를 계산하고자 하는 사람 x, y 중 x와 연결된 다른 노드들의 거리를 구한다
# 결과로 얻어진 distance[y]를 출력하면 x와 y의 거리
bfs(x)
print(distance[y])
