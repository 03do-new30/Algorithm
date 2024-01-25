import sys
input = sys.stdin.readline
from collections import namedtuple

# Stable Sort
# 값이 같을 때, 입력 순서가 항상 유지되어야 한다
Member = namedtuple('Member', ['age', 'name', 'order'])
n = int(input())
arr = []
for i in range(n):
    tmp = input().split()
    arr.append(Member(int(tmp[0]), tmp[1], i))

arr.sort(key = lambda x : (x.age, x.order))
for x in arr:
    print(x.age, x.name)
