def gift_score(log, i):
    give = sum(log[i])
    take = 0
    for j in range(len(log)):
        take += log[j][i]
    return give - take
    
def solution(friends, gifts):
    n = len(friends)
    fr_idx = dict()
    for i in range(n):
        fr_idx[friends[i]] = i
    # 선물을 주고받은 기록을 인접 행렬로 나타냄
    # log[i][j] = i번째 친구가 j번째 친구에게 몇번 선물을 주었는가
    log = [[0] * n for _ in range(n)]
    for data in gifts:
        giver, taker = data.split()
        log[fr_idx[giver]][fr_idx[taker]] += 1
    
    # i와 j 두 사람 사이의 기록으로 다음달 선물을 예측한다
    result = [0] * n # 다음달 선물 예측하여 기록, result[i] = i번째 사람이 다음달에 받게 될 선물의 수
    
    for i in range(n-1):
        for j in range(i+1, n):
            if log[i][j] > log[j][i]:
                result[i] += 1
                continue
            if log[j][i] > log[i][j]:
                result[j] += 1
                continue
            
            i_score = gift_score(log, i)
            j_score = gift_score(log, j)
            if i_score > j_score:
                result[i] += 1
                continue
            if j_score > i_score:
                result[j] += 1
                continue
            # i_score == j_score인 경우 아무일도 일어나지 않는다
    
    # print("result:", result)
    return max(result)
            
            