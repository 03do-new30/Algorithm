import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split(' '))
q = deque()

for i in range(1, n+1):
    q.append(i)

answer = []

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(str(q.popleft()))

print('<' + ', '.join(answer) + '>')