from collections import deque
from copy import deepcopy
def solution(edges, target):
    # 노드 개수
    n = len(target)
    # edges를 이용해 그래프(인접리스트)로 변경해두자
    # 이때 deque를 사용하면 길이 업데이트 되는 것을 구현하기 쉬움
    graph = [[] for _ in range(n+1)]
    for u, v in edges:
        graph[u].append(v)
        graph[u].sort()
    for i in range(len(graph)):
        graph[i] = deque(graph[i])
    
    
    def travel(graph):
        # 길을 지나면서 업데이트하고, 도착하는 리프 노드의 번호를 반환한다
        node = 1
        while graph[node]:
            next_node = graph[node].popleft()
            graph[node].append(next_node) # 현재 지나온 노드를 가장 뒤로 보내면서 길을 자동으로 업데이트한다
            # update
            node = next_node
        return node
    
    # 업데이트를 반복하다보면 최초의 그래프 상태로 돌아오는 순간이 반복될 것이다
    # 그 사이클 동안의 리프노드 방문 순서를 얻어내자
    original_graph = deepcopy(graph)
    first = True
    leaf_cycle = []
    while first or graph != original_graph:
        if first:
            first = False
        leaf = travel(graph)
        leaf_cycle.append(leaf)
    
    # print("leaf_cycle:", leaf_cycle)
    
    # 어떤 노드 i를 n번 방문할 때,
    # 1 * n <= target[i-1] <= 3 * n을 만족한다면 
    # n번의 방문은 target[i-1]를 만들 수 있는 "최소 방문 횟수"임
    min_visit = [0] * n
    for i in range(n):
        if target[i] == 0:
            continue
        for cnt in range(1, 101):
            if cnt <= target[i] <= 3 * cnt:
                min_visit[i] = cnt
                break
    # print("min_visit:", min_visit)

    # leaf_cycle을 돌면서 
    # min_visit 이상이 될 수 있도록 방문 순서를 구성한다
    visit_cnt = [0] * n
    visit_check = [False] * n
    for i in range(n):
        if min_visit[i] == 0:
            visit_check[i] = True
    visit_order = []

    idx = 0
    while False in visit_check:
        if idx >= len(leaf_cycle):
            idx = 0
        leaf = leaf_cycle[idx]
        visit_order.append(leaf)
        leaf_idx = leaf - 1
        visit_cnt[leaf_idx] += 1
        if visit_cnt[leaf_idx] >= min_visit[leaf_idx]:
            visit_check[leaf_idx] = True
        idx += 1
    # print("visit_order:", visit_order)
    # print("visit_cnt:", visit_cnt)

    # 만약 visit_cnt가 target을 초과하는 경우가 있다면 불가능 -> return [-1]
    for i in range(n):
        if visit_cnt[i] > target[i]:
            return [-1]
    
    

    def make_num(num, cnt):
        # cnt 번 더해서 num을 만드는 방법
        result = []
        while cnt > 0:
            remain = num - sum(result)
            if 1 + (cnt-1) <= remain <= 1 + 3 * (cnt-1):
                result.append(1)
                cnt -= 1
            elif 2 + (cnt-1) <= remain <= 2 + 3 * (cnt - 1):
                result.append(2)
                cnt -= 1
            elif 3 + (cnt-1) <= remain <= 3 + 3 * (cnt - 1):
                result.append(3)
                cnt -= 1
        return result
    
    # vsit_cnt를 참고하여 숫자의 합을 구성해본다
    card_order = [deque() for _ in range(n)]
    for i in range(n):
        if visit_cnt[i] == 0:
            continue
        card_order[i] = deque(make_num(target[i], visit_cnt[i]))
    # print("card_order:", card_order)

    result = []
    for leaf in visit_order:
        card = card_order[leaf-1].popleft()
        result.append(card)
    # print("result:", result)
    return result
    

edges = [
    [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]],
    [[1, 2], [1, 3]],
    [[1, 3], [1, 2]]
    ]
target = [
    [0, 0, 0, 3, 0, 0, 5, 1, 2, 3],
    [0, 7, 3],
    [0, 7, 1]
]
result = [
    [1, 1, 2, 2, 2, 3, 3],
    [1, 1, 3, 2, 3],
    [-1]
]

for i in range(len(result)):
    print(solution(edges[i], target[i]) == result[i])
    print('-' * 40)