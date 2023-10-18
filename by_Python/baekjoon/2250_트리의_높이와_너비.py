import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# node[i] = [부모노드, 왼쪽노드, 오른쪽노드]
node = [[-1, -1, -1] for _ in range(n+1)]

### 1 ###
# 노드 저장
for _ in range(n):
    value, left, right = map(int, input().split())
    node[value][1] = left
    node[value][2] = right
    # 부모 노드 저장
    if left != -1:
        node[left][0] = value
    if right != -1:
        node[right][0] = value

### 2 ###
# 루트 노드를 찾는다
root = -1
for i in range(1, n+1):
    if node[i][0] == -1:
        root = i 
        break

### 3 ###
# 각 노드별 레벨을 구한다
level = [-1] * (n+1)
# bfs
def find_level(start):
    q = deque()
    q.append(start)
    level[start] = 1
    while q:
        current = q.popleft()
        left = node[current][1]
        right = node[current][2]
        if left != -1 and level[left] == -1:
            level[left] = level[current] + 1
            q.append(left)
        if right != -1 and level[right] == -1:
            level[right] = level[current] + 1
            q.append(right)
find_level(root)

### 4 ###
# 노드의 컬럼 번호는 놀랍게도 IN ORDER 방문순서이다!
order = [-1]
def in_order(start):
    left = node[start][1]
    right =node[start][2]
    # left
    if left != -1:
        in_order(left)
    # node
    order.append(start)
    # right
    if right != -1:
        in_order(right)
in_order(root)
# order에는 방문한 순서대로 노드들이 들어가있는데,
# node_order[x] = x노드의 방문 순서가 될 수 있도록 가공한다
node_order = [-1] * (n+1)
for i in range(1, n+1):
    x = order[i]
    node_order[x] = i

### 4 ###
# 레벨별로 너비를 출력한다
max_level = max(level)
level_width = [-1] * (max_level + 1) # 레벨별 너비를 저장함
for lv in range(1, max_level + 1):
    # level에서 lv 레벨을 갖는 모든 노드들을 추출한다
    lv_nodes = []
    for i in range(1, n+1):
        if level[i] == lv:
            lv_nodes.append(i)
    # lv_nodes 노드들의 in-order 방문순서를 구한다
    lv_orders = []
    for x in lv_nodes:
        lv_orders.append(node_order[x])
    # lv 레벨의 너비를 구한다
    width = max(lv_orders) - min(lv_orders) + 1
    # level_width에 너비를 저장한다
    level_width[lv] = width

### 5 ###
# 정답 출력!
width_answer = max(level_width)
for lv in range(1, max_level + 1):
    if level_width[lv] == width_answer:
        print(lv, width_answer)
        break
