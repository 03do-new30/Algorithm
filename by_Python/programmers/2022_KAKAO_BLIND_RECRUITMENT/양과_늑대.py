def solution(info, edges):
    n = len(info)
    # 인접 리스트
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    max_sheep = 0
    
    def dfs(node, visited, sheep, wolf, log):
        nonlocal max_sheep

        # 현재 상태에서 방문할 수 있는 노드들은
        # 내가 방문한 노드들의 자식들 중 아직 방문하지 않은 노드들
        visitables = []
        for i in range(n):
            if visited[i]:
                children = graph[i]
                for child in children:
                    if not visited[child]:
                        if child not in visitables:
                            visitables.append(child)
        
        for next_node in visitables:
            if visited[next_node]:
                continue
            
            next_sheep = sheep; next_wolf = wolf
            if info[next_node] == 0:
                next_sheep += 1
            else:
                next_wolf += 1
            
            # sheep <= wolf이면 가지 않는다
            if next_sheep <= next_wolf:
                continue

            visited[next_node] = True
            dfs(next_node, visited, next_sheep, next_wolf, log + [next_node])
            visited[next_node] = False
        # sheep을 max_sheep이랑 비교해본다
        # print("log:", log, "sheep:", sheep)
        max_sheep = max(max_sheep, sheep)

    visited = [False] * n
    visited[0] = True
    dfs(0, visited, 1, 0, [0])
    

    # 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아 다시 루트 노드로 돌아온다
    answer = max_sheep # 모을 수 있는 양은 최대 몇마리인지
    # print("max_sheep:", max_sheep)
    return answer

info = [
    [0,0,1,1,1,0,1,0,1,0,1,1],
    [0,1,0,1,1,0,1,0,0,1,0]	
]
edges = [
    [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]],
    [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
]
result = [5, 5]
for i in range(len(result)):
    print(solution(info[i], edges[i]) == result[i])
    print('-' * 40)