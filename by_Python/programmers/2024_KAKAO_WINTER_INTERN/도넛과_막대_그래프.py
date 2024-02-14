def solution(edges):
    mx_node = max(map(max, edges))
    
    # edges 정보를 바탕으로 in_degree, out_degree를 구함
    in_degree = [0] * (mx_node + 1)
    out_degree = [0] * (mx_node + 1)
    for u, v in edges:
        out_degree[u] += 1
        in_degree[v] += 1
    
    # 생성된 정점 = 나가는 edge가 두개 이상, 들어오는 edge가 없음
    new_node = -1
    for u in range(1, mx_node + 1):
        if out_degree[u] >= 2 and in_degree[u] == 0:
            new_node = u
            break
    
    # 전체 그래프의 개수는 new_node에 연결된 간선의 개수
    total = out_degree[new_node]

    # 그래프 산정 시 혼동을 방지하기 위해 new_node와 연결된 간선들을 모두 삭제한다
    out_degree[new_node] = 0
    for u, v in edges:
        if u == new_node:
            in_degree[v] -= 1
    
    # (1) 막대: 반드시 하나의 정점은 해당 정점으로 아무런 간선도 진입하지 않는다
    sticks = 0
    for u in range(1, mx_node + 1):
        if u == new_node:
            continue
        if in_degree[u] == 0:
            sticks += 1
            continue
    
    # (2) 8자: 반드시 하나의 정점(교차되는 부분)은 들어오는 간선 2개, 나가는 간선 2개
    eights = 0
    for u in range(1, mx_node + 1):
        if u == new_node:
            continue
        if in_degree[u] == 2 and out_degree[u] == 2:
            eights += 1
    
    # (3) 도넛: 전체 그래프에서 막대, 8자를 제외하고 남아있는 그래프 개수
    donuts = total - sticks - eights
    # 생성한 정점의 번호, 도넛모양 그래프의 수, 막대모양 그래프의 수, 8자모양 그래프의 수를 리턴
    return [new_node, donuts, sticks, eights]

### 입출력 예
inputs = [
            [[2, 3], [4, 3], [1, 1], [2, 1]],
            [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
        ]
results = [[2, 1, 1, 0], [4, 0, 1, 2]]

for i in range(2):
    print('#', i+1)
    print(results[i] == solution(inputs[i]))