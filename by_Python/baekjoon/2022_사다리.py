import sys, math
input = sys.stdin.readline

"""
codeplus 해설 참고
"""
x, y, c = map(float, input().split())

left = 0
right = min(x, y)

while abs(right - left) > 1e-6:
    mid = (left + right) / 2
    d = mid
    h1 = math.sqrt(x*x - d*d)
    h2 = math.sqrt(y*y - d*d)
    h = (h1 * h2) / (h1 + h2)
    if h > c:
        left = mid
    else:
        right = mid
print(left)