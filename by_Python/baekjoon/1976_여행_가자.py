import sys
input = sys.stdin.readline


def find(i):
    # 노드 i의 부모를 찾는다
    if parents[i] == i:
        return i
    parents[i] = find(parents[i])
    return parents[i]


def union_find(i, j):
    # 연결되어 있는 노드i - 노드j 유니온파인드
    i = find(i)
    j = find(j)
    if i < j:
        parents[j] = i
    elif i > j:
        parents[i] = j
    else:
        return


N = int(input().strip())
M = int(input().strip())
graph = [[0]*(N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

# union-find, disjoint-set
parents = [0] + [x for x in range(1, N+1)]  # 부모 노드 번호 저장
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == 1:
            union_find(i, j)

# union-find 이후 plan에 속한 도시들을 x라고 하면
# parents[x]가 모두 같은 값이면 여행이 가능하다
ans = "YES"
for i in range(len(plan) - 1):
    if parents[plan[i]] != parents[plan[i+1]]:
        ans = "NO"
        break
print(ans)
