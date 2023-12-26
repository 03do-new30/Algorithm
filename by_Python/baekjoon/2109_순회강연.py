import sys
input = sys.stdin.readline
from collections import namedtuple
import heapq
# 보석 도둑 문제와 유사하나, 내림차순으로 정렬

info = namedtuple("info", ["day", "price", "lecture"])
n = int(input())
arr = []
max_day = 0 # 강연을 할 수 있는 기간
for _ in range(n):
    p, d = map(int, input().split())
    max_day = max(max_day, d)
    arr.append(info(d, p, True))

# 날짜도 arr에 함께 넣어줌
for x in range(1, max_day + 1):
    arr.append(info(x, 0, False))

arr.sort(key = lambda x : -x[0]) # 날짜 내림차순 정렬
# print("arr:", arr)
heap = []
answer = 0
for i in range(len(arr)):
    if arr[i].lecture: # 강의인 경우
        heapq.heappush(heap, -arr[i].price)
    else: # 강의가 아니라 날짜인 경우
        if heap:
            answer -= heapq.heappop(heap)

print(answer)