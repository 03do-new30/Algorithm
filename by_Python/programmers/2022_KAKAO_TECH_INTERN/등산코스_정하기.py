import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    
    INF = float('inf')

    # 출입구 -> 산봉우리의 최소 intensity만 알아도 문제를 해결할 수 있다
    # 그래프 조정:
    ### 출입구에 연결된 등산로 -> 출입구에서 다른 지점으로만 이동 가능한 단방향 등산로
    ### 산봉우리에 연결된 등산로 -> 다른 지점에서 산봉우리로만 갈 수 있는 단방향 등산로
    graph = defaultdict(list)
    
    # x in gates, x in summits 연산을 빠르게 하기 위해
    is_gate = [False] * (n+1)
    for gate in gates:
        is_gate[gate] = True
    is_summit = [False] * (n+1)
    for summit in summits:
        is_summit[summit] = True
    
    for a, b, c in paths:
        if is_gate[a] or is_summit[b]:
            graph[a].append((b, c))
        elif is_summit[a] or is_gate[b]:
            graph[b].append((a, c))
        else:
            graph[a].append((b, c))
            graph[b].append((a, c))

    # 모든 출입구에서 한번씩 다익스트라 알고리즘을 실행한다면 시간 초과
    # 어느 출입구에서 출발하는지에 상관 없이 intensity의 최소값과 산봉우리의 번호만 알면 된다
    # 한 번의 다익스트라에서 모든 출입구를 시작 정점으로 두고 알고리즘을 실행하자
    dist = [INF] * (n+1)
    q = [] # 우선순위 큐 활용
    for gate in gates:
        dist[gate] = 0
        heapq.heappush(q, (0, gate))
    
    while q:
        d, i = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 것이라면 무시한다
        ########### 와 이거 추가하니까 21번 테케 시간초과 풀림 ###########
        if dist[i] < d:
            continue
         ########### ###########
        for j, wt in graph[i]:
            intensity = max(wt, d) # intensity는 현재까지 지난 간선에서 가장 가중치가 큰 값
            if dist[j] > intensity:
                # 우리는 intensity의 최소값을 알고싶다
                dist[j] = intensity
                # 정상인 경우에는 q에 넣지 않음
                if is_summit[j]:
                    continue
                heapq.heappush(q, (intensity, j))

    
    # dist[summit]은 출입구에서 summit까지의 intensity
    # print("dist:", dist)
    summits.sort()
    answer = [-1, INF]
    for summit in summits:
        if dist[summit] < answer[1]:
            answer = [summit, dist[summit]]
    # print("answer:", answer)
    return answer


n = [6, 7, 7, 5]
paths = [
    [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
    [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]	,
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
]
gates = [[1, 3],[1],[3, 7],[1, 2]]
summits = [[5], [2, 3, 4], [1, 5], [5]]
result = [[5, 3], [3, 4], [5, 1], [5, 6]]

for i in range(len(result)):
    print(solution(n[i], paths[i], gates[i], summits[i]) == result[i])
    print('-' * 40)