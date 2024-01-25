import sys
input = sys.stdin.readline
from collections import namedtuple

n = int(input())
arr = [int(input()) for _ in range(n)]

# 실제로 버블 소트를 실행하는 것은 시간이 너무 오래 걸린다!
# 버블소트의 특징
# 앞에 있는 수가 뒤로 가는 것은 몇칸이든 가능하나
# 뒤에 있던 수가 앞으로 오는 것은 한 사이클에 한 칸씩밖에 못옴!
# 정렬된 배열과 비교해서 앞으로 몇번 와야하는지 계산, 앞으로 이동해야하는 칸수의 최대가 정답이다

# number = 수, prev_idx = 정렬 전의 위치
Point = namedtuple('Point', ['number', 'prev_idx'])
target = []
for i in range(n):
    target.append(Point(arr[i], i))

target.sort()

answer = 0
for i in range(n):
    tmp = target[i].prev_idx - i
    if tmp > answer:
        answer = tmp
print(answer + 1)
