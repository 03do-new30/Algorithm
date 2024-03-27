from collections import deque

def solution(queue1, queue2):
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1
    
    n = len(queue1)

    answer = 0
    repeat = 4 * n
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    while sum_q1 != sum_q2:
        if answer > repeat:
            return -1
        if sum_q1 > sum_q2:
            popped = queue1.popleft()
            queue2.append(popped)
            sum_q1 -= popped
            sum_q2 += popped
        else:
            popped = queue2.popleft()
            queue1.append(popped)
            sum_q2 -= popped
            sum_q1 += popped
        answer += 1
    return answer


queue1 = [
    [3, 2, 7, 2],
    [1, 2, 1, 2],
    [1, 1]
]

queue2 = [
    [4, 6, 5, 1],
    [1, 10, 1, 2],
    [1, 5]
]

result = [2, 7, -1]

for i in range(len(result)):
    print(solution(queue1[i], queue2[i]) == result[i])
    print('-' * 40)