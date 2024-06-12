import sys
import heapq
input = sys.stdin.readline

# max_heap과 min_heap을 동시에 둔다
# 항상 max_heap과 min_heap의 원소 개수 차이가 1개 이상이게 두고
# max_heap이 min_heap보다 한개 더 많게 한다
# 항상 min_heap의 꼭대기 원소가 max_heap의 꼭대기 원소보다 커야 한다
max_heap = []
min_heap = []
heapq.heapify(max_heap)
heapq.heapify(min_heap)

n = int(input())
for i in range(n):
    num = int(input())
    if i == 0:
        heapq.heappush(max_heap, -num)
    elif i == 1:
        if num > -max_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
            heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(max_heap, -num)
        if -max_heap[0] > min_heap[0]:
            # num을 다시 min_heap에 넣어준다
            heapq.heappop(max_heap)
            heapq.heappush(min_heap, num)
            # size 검사
            if len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
        if len(max_heap) - len(min_heap) > 1:
            # max_heap에 있는 원소를 min_heap으로 옮겨줘야 함
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    # print("max_heap:", max_heap)
    # print("min_heap:", min_heap)
    print(-max_heap[0])
    # print('-' * 30)
