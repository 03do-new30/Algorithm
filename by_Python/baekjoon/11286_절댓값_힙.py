import sys
input = sys.stdin.readline

import heapq
from collections import defaultdict

heap = []
negative = defaultdict(int)

N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if heap:
            popped = heapq.heappop(heap)
            if negative[popped] > 0:
                print(-popped)
                negative[popped] -= 1
            else:
                print(popped)
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(heap, -x)
            negative[-x] += 1
        else:
            heapq.heappush(heap, x)