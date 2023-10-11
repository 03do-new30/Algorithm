import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 인접리스트
a = [[] for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    a[i].append(j)
    a[j].append(i)

# 친구 5명이 연결되면 True!
def solve(node, visited, count):
    # print("node:",node, "visited:", visited, "count:", count)
    if count == 5:
        return True
    
    for next in a[node]:
        if not visited[next]:
            visited[next] = True
            ret = solve(next, visited, count + 1)
            visited[next] = False
            if ret:
                return True
    
    return False

for start in range(n):
    visited = [False] * n
    visited[start] = True
    ret = solve(start, visited, 1)
    if ret:
        print(1)
        exit()
print(0)
