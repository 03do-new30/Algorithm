import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(a):
    if a == sets[a]:
        return a
    sets[a] = find(sets[a])
    return sets[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        sets[b] = a
    elif a > b:
        sets[a] = b
    else:
        return


def check(a, b):
    if find(a) == find(b):
        print("YES")
    else:
        print("NO")


n, m = map(int, input().split())
sets = [x for x in range(n+1)]  # 자기 자신으로 초기화
for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        check(a, b)
