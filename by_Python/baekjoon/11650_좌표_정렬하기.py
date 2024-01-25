import sys
input = sys.stdin.readline
from collections import namedtuple

Point = namedtuple('Point', ['x','y'])
n = int(input())
arr = [Point(*map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda point : (point.x, point.y))

for p in arr:
    print(p.x, p.y)
