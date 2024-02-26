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

    # a_scores와 b_scores를 비교하여, 주사위 조합별 a가 이긴 횟수를 저장한다
    a_wins = []
    for i in range(len(a_scores)):
        a_win = 0
        print("a_scores[i]:", a_scores[i])
        print("b_scores[i]:", b_scores[i])
        print("-" * 30)
        for j in range(len(a_scores[i])):
            if a_scores[i][j] > b_scores[i][j]:
                a_win += 1
        a_wins.append(a_win)
    print("a_wins:", a_wins)
    # a_wins에서 이긴 횟수가 가장 많은 인덱스번째 조합이 a가 승리할 확률이 가장 높은 주사위 조합이다
    max_wins = max(a_wins)
    max_idx = 0
    for i in range(len(a_wins)):
        if a_wins[i] == max_wins:
            max_idx = i
            break
    
    # A가 골라야 하는 주사위 번호를 오름차순으로 return
    result = []
    for x in a_combis[max_idx]:
        result.append(x + 1)
    result.sort()
    return result
    
        
                
inputs = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]

results = [[1, 4], [2], [1, 3]]

for i in range(3):
    print(solution(inputs[i]) == results[i])
    print('=' * 40)