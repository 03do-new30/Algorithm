import sys
from collections import defaultdict
input = sys.stdin.readline


def delete(x):
    # -2 = 삭제됨을 의미
    parents[x] = -2

    # x를 부모로 가지는 노드들도 삭제
    for i in range(N):
        if parents[i] == x:
            delete(i)


N = int(input().strip())
parents = list(map(int, input().split()))
del_node = int(input().strip())

# 노드 삭제
delete(del_node)

# 리프노드의 개수 세기
# -2 표시가 되어있지 않고, 다른 노드의 부모가 아닌 것을 찾는다
ans = 0
for i in range(N):
    if parents[i] != -2 and i not in parents:
        ans += 1
print(ans)
