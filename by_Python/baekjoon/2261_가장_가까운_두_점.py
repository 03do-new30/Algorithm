import sys
from collections import namedtuple
input = sys.stdin.readline
Point = namedtuple('Point', ['x', 'y'])

"""
해설, 소스코드 참고
"""

n = int(input())
ax = [Point(*map(int, input().split())) for _ in range(n)]
ay = ax[:]
ax.sort() # x 기준 정렬
ay.sort(key=lambda point : (point.y, point.x)) # y 기준 정렬

def dist(p1:Point, p2:Point):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2

def brute_force(a, start, end):
    ans = -1
    for i in range(start, end):
        for j in range(i+1, end+1):
            d = dist(a[i], a[j])
            if ans == -1 or ans > d:
                ans = d
    return ans

def closest(ax, ay, start, end):
    n = end - start + 1
    if n <= 3:
        return brute_force(ax, start, end)
    
    mid = (start + end) // 2
    mid_p = ax[mid]
    ay_left = []
    ay_right = []
    
    for p in ay:
        if p <= mid_p:
            ay_left += [p]
        else:
            ay_right += [p]
    
    left = closest(ax, ay_left, start, mid)
    right = closest(ax, ay_right, mid + 1, end)
    ans = min(left, right)

    b = []
    for p in ay:
        d = p.x - mid_p.x
        if d * d < ans:
            b += [p]
    
    m = len(b)
    for i in range(m-1):
        for j in range(i+1, m):
            y = b[j].y - b[i].y
            if y * y < ans:
                d = dist(b[i], b[j])
                if d < ans:
                    ans = d
            else:
                break
    
    return ans

print(closest(ax, ay, 0, n-1))