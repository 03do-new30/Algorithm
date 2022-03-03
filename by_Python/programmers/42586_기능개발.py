# 배포되어야하는 순서대로 작업의 진도가 적힌 progresses
# 작업의 개발 속도가 적힌 정수 배열 speeds
# 각 배포마다 몇 개의 기능이 배포되는가?
import math
from collections import deque


def solution(progresses, speeds):
    # 완료까지 걸리는 일 수
    q = deque([])
    for i in range(len(progresses)):
        remains = 100 - progresses[i]
        q.append(math.ceil(remains / speeds[i]))

    answer = []

    while q:
        first_feature = q.popleft()
        ans = 1

        while q:
            if q[0] <= first_feature:
                q.popleft()
                ans += 1
            else:
                break

        answer.append(ans)

    return answer
