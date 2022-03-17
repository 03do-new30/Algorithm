import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        # 모든 음식의 스코빌 지수를 K이상으로 만들 수 없음 = 더이상 섞을 것이 없음
        if len(scoville) < 2:
            return -1
        mix = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, mix)
        answer += 1
    return answer
