from collections import deque
import sys

sys.stdin = open("by_Python/SWEA/inputs/보물상자_비밀번호.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    q = deque(list(input())) # deque 형태로 자료구조 변경
    
    # 한 변에 들어가는 수
    side_capacity = n // 4
    
    repeat = 0
    num_set = set() # 도출되는 숫자들 저장
    while repeat != side_capacity:
        for i in range(0, n, side_capacity):
            str = ""
            for j in range(side_capacity):
                str += q[i+j]
            num_set.add(str)
        # q를 시계방향으로 움직인다
        q.appendleft(q.pop())
        repeat += 1
    
    # num_set에 저장된 16진수들을 10진수 숫자로 변환하여 저장하자
    tmp = list(num_set)
    result = []
    for string in tmp:
        result.append(int('0x' + string, 16))
    result.sort(reverse=True)

    
    answer = result[k-1]
    print("#{0} {1}".format(test_case, answer))
