from itertools import combinations

def get_scores(dice, combis):
    scores = []
    limit = len(dice) // 2
    for combi in combis:
        current = []
        for i1 in range(6):
            tmp1 = dice[combi[0]][i1]
            if limit == 1:
                current.append(tmp1)
                continue
            
            for i2 in range(6):
                tmp2 = tmp1 + dice[combi[1]][i2]
                if limit == 2:
                    current.append(tmp2)
                    continue
                
                for i3 in range(6):
                    tmp3 = tmp2 +  dice[combi[2]][i3]
                    if limit == 3:
                        current.append(tmp3)
                        continue
                    
                    for i4 in range(6):
                        tmp4 = tmp3 + dice[combi[3]][i4]
                        if limit == 4:
                            current.append(tmp4)
                            continue
                        
                        for i5 in range(6):
                            tmp5 = tmp4 + dice[combi[4]][i5]
                            current.append(tmp5)
        scores.append(current)
    return scores

def solution(dice):
    n = len(dice)
    # A가 가져가는 주사위 조합
    a_combis = list(combinations(range(n), n//2))
    # B가 가져가는 주사위 조합
    b_combis = []
    for a_combi in a_combis:
        tmp = []
        for x in range(n):
            if x not in a_combi:
                tmp.append(x)
        b_combis.append(tuple(tmp))
    
    # A가 가져가는 주사위 조합의 점수들
    a_scores = get_scores(dice, a_combis)
    # B가 가져가는 주사위 조합의 점수들
    b_scores = get_scores(dice, b_combis)

    # a가 b를 이기는 경우가 많은 a의 주사위 조합을 winner에 저장
    winner = [-1, -1]
    cnt = 0
    for idx in range(len(a_scores)):
        a_win = 0
        for a_idx in range(len(a_scores[0])):
            for b_idx in range(len(b_scores[0])):
                if a_scores[idx][a_idx] > b_scores[idx][b_idx]:
                    a_win += 1
        if a_win > cnt:
            winner = [x+1 for x in a_combis[idx]]
            cnt = a_win
    
    return winner
    
        
                
inputs = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]

results = [[1, 4], [2], [1, 3]]

for i in range(3):
    print(solution(inputs[i]) == results[i])
    print('=' * 40)