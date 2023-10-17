import sys
input = sys.stdin.readline

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

tree = dict()

n = int(input())
for _ in range(n):
    node, left, right = input().split()
    tree[node] = Node(left, right)

pre_result = []
def pre_order(x):
    node = tree[x]
    pre_result.append(x)
    # left
    if node.left != '.':
        pre_order(node.left)
    # right
    if node.right != '.':
        pre_order(node.right)

in_result = []
def in_order(x):
    node = tree[x]
    # left
    if node.left != '.':
        in_order(node.left)
    # node
    in_result.append(x)
    # right
    if node.right != '.':
        in_order(node.right)

post_result = []
def post_order(x):
    node = tree[x]
    # left
    if node.left != '.':
        post_order(node.left)
    # right
    if node.right != '.':
        post_order(node.right)
    # node
    post_result.append(x)

pre_order('A')
print(''.join(pre_result))
in_order('A')
print(''.join(in_result))
post_order('A')
print(''.join(post_result))

    