import sys
from collections import namedtuple
from math import sqrt
input = sys.stdin.readline
Point = namedtuple('Point', ['x', 'y', 'z'])

"""
codeplus 해설 참고 - 삼분법이라는 게 있다는 것만 알아두기
"""
ins = list(map(float, input().split()))
a = Point(ins[0], ins[1], ins[2])
b = Point(ins[3], ins[4], ins[5])
c = Point(ins[6], ins[7], ins[8])

# 삼차원상의 점 u와 점 v사이의 거리
def get_dist(u, v):
    return sqrt((u.x- v.x)**2 + (u.y - v.y)**2 + (u.z-v.z)**2)

# 선분 AB의 점 중에서 점 C와 가장 가까운 거리의 점을 찾는다
# 삼분 탐색 이용
left = 0.0
right = 1.0
m = 0
dx = b.x - a.x
dy = b.y - a.y
dz = b.z - a.z
while True:
    if abs(right - left) < 1e-9:
        m = (left + right) / 2
        break
    m1 = left + (right - left) / 3
    m2 = right - (right - left) / 3
    m1_point = Point(a.x + m1*dx, a.y + m1*dy, a.z + m1*dz)
    m2_point = Point(a.x + m2*dx, a.y + m2*dy, a.z + m2*dz)
    d1 = get_dist(m1_point, c)
    d2 = get_dist(m2_point, c)
    if d1 > d2:
        left = m1
    else:
        right = m2

final = Point(a.x + m*dx, a.y+ m*dy, a.z + m*dz)
ans = get_dist(final, c)
print('%.10f' %ans)