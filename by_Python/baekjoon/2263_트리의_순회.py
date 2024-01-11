import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# inorder에서 계속 root node의 위치를 찾아줘야 하는 것은 비효율적
# position 리스트를 이용해 시간초과 피하자
# position[i] = 정점 i가 inorder 내에서 차지하는 순서를 저장한다
# inorder[position[i]] = i
position = [0] * (n+1)
for i in range(n):
    position[in_order[i]] = i

pre_order = []
def solve(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    
    # 최상단의 루트 노드는 post_order의 마지막 순회 노드
    root = post_order[post_end]
    print(root, end=' ') # preorder: root 출력

    # 루트의 위치
    p = position[root]

    # inorder: in_start, p, in_end
    # postorder: post_start, post_end
    # left node의 개수 : p - in_start
    # right node의 개수: in_end - p
    left = p - in_start
    # preorder: left 출력
    solve(in_start, p-1, post_start, post_start + left - 1)
    # preorder: right 출력
    solve(p+1, in_end, post_start + left, post_end -1)


solve(0, n-1, 0, n-1)
print()