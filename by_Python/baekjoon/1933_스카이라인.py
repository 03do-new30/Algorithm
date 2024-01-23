import sys
from collections import namedtuple
input = sys.stdin.readline
Building = namedtuple('Building', ['left', 'height', 'right'])
Pair = namedtuple('Pair', ['x', 'height'])

"""
해설과 소스코드 참고
mergesort와 유사하게 분할정복으로 풀이 가능
"""

def go(a: [Building], start, end):
    if start == end:
        return [
            Pair(a[start].left, a[start].height),
            Pair(a[start].right, 0) # 건물 끝점의 높이는 0으로
        ]
    
    mid = (start + end) // 2
    l = go(a, start, mid)
    r = go(a, mid + 1, end)

    return merge(l, r)

def append(ans:[Pair], p:Pair):
    if ans:
        if ans[-1].height == p.height:
            # 중복되는 높이는 기록하지 않는다
            return
        if ans[-1].x == p.x:
            ans[-1] = Pair(ans[-1].x, p.height)
            return
    ans += [p]

def merge(l:[Pair], r:[Pair]):
    ans = []
    h1 = 0 # 왼쪽 스카이라인의 현재 높이
    h2 = 0 # 오른쪽 스카이라인의 현재 높이
    i = 0 # left index
    j = 0 # right index

    while i < len(l) and j < len(r):
        u = l[i]
        v = r[j]
        if u.x < v.x:
            # x좌표가 더 작다면 결과에 추가
            # 이때, 높이는 h1 h2 중 더 높은 것으로 추가한다
            x = u.x
            h1 = u.height
            h = max(h1, h2)
            append(ans, Pair(x, h))
            i += 1
        else:
            # x좌표가 더 작다면 결과에 추가
            # 이때, 높이는 h1 h2 중 더 높은 것으로 추가한다
            x = v.x
            h2 = v.height
            h = max(h1, h2)
            append(ans, Pair(x, h))
            j += 1
    
    while i < len(l):
        append(ans, l[i])
        i += 1
    
    while j < len(r):
        append(ans, r[j])
        j += 1
    
    return ans

n = int(input())
a = [Building(*map(int, input().split())) for _ in range(n)]
a.sort()
ans = go(a, 0, n-1)

for x, height in ans:
    sys.stdout.write('%d %d ' % (x, height))
sys.stdout.write('\n')