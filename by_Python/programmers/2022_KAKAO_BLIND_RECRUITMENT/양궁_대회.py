# 참고 (https://velog.io/@syong_e/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8CDFS-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
from itertools import product
def solution(n, info):
    global max_gap, answer
    
    answer = [-1]
    ryan = [0] * 11
    max_gap = 0

    def is_winner_with_gap(ryan):
        a = 0 # 어피치 점수
        b = 0 # 라이언 점수
        for i in range(11):
            if info[i] > 0 or ryan[i] > 0:
                if info[i] >= ryan[i]:
                    a += (10 - i)
                else:
                    b += (10 - i)
        return (b > a, abs(a - b))
    
    # idx: info리스트의 인덱스
    # cnt: 쏜 화살의 개수
    def dfs(idx, cnt):
        global max_gap, answer
        if idx == 11 or cnt == 0: # 종료 조건
            is_winner, gap = is_winner_with_gap(ryan)
            if is_winner:
                if cnt >= 0: # 화살이 남아있는 경우
                    ryan[10] = cnt # 0점에 몰아넣기
                
                if gap > max_gap:
                    max_gap = gap
                    answer = ryan.copy()
                elif gap == max_gap: # 가장 낮은 점수를 많이 맞힌 경우로 업데이트
                    for i in range(11):
                        if answer[i] > 0:
                            max_i_1 = i
                        if ryan[i] > 0:
                            max_i_2 = i
                    if max_i_2 > max_i_1:
                        answer = ryan.copy()
            return
        # 어피치보다 많이 맞춘다
        if cnt > info[idx]:
            ryan[idx] = info[idx] + 1
            dfs(idx + 1, cnt - (info[idx] + 1))
            ryan[idx] = 0 # 백트래킹

        # 아예 안맞춘다
        dfs(idx + 1, cnt)

    dfs(0, n)
    return answer

n = [5, 1, 9, 10]
info = [[2,1,1,1,0,0,0,0,0,0,0]	,
        [1,0,0,0,0,0,0,0,0,0,0]	,
        [0,0,1,2,0,1,1,1,1,1,1]	,
        [0,0,0,0,0,0,0,0,3,4,3]	]
result = [ [0,2,2,0,1,0,0,0,0,0,0],
          [-1],
          [1,1,2,0,1,2,2,0,0,0,0],
          [1,1,1,1,1,1,1,1,0,0,2]]
for i in range(len(result)):
    sol = solution(n[i], info[i])
    print(result[i] == sol)
    print('-' * 40)