import sys
input = sys.stdin.readline
import heapq
from collections import namedtuple

n, k = map(int, input().split())
arr = []
Info = namedtuple("Info", ["wt", "val", "bag"]) # bag True이면 가방
for _ in range(n):
   wt, val = map(int, input().split())
   arr.append(Info(wt, val, False))
for _ in range(k):
   wt = int(input())
   arr.append(Info(wt, 0, True))

arr.sort(key = lambda x : x[0])

answer = 0
heap = [] # 가격 저장하는 maxheap으로 사용한다
last_idx = 0
for i in range(len(arr)):
   if arr[i].bag:
    # 앞에 있는 후보들을 힙에 추가
    idx = last_idx
    while idx < i:
        heapq.heappush(heap, -arr[idx].val)
        idx += 1
    answer -= heapq.heappop(heap) # 후보들 중 가장 가격이 높은 보석을 넣는다
    last_idx = idx
print(answer)

    
         
   

"""
3 2 
1 100
5 55555
2 100000
10
2
"""
# jewles: [(1, 100), (2, 100000), (5, 55555)] bags: [2, 10]
# answer: 100100
# 155555가 답이어야한다