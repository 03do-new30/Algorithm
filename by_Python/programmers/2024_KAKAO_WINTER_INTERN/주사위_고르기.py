from itertools import combinations

def get_scores(dice, combi):
    n = len(combi)
    scores = []
    for i1 in range(6):
        tmp1 = dice[combi[0]][i1]
        if n == 1:
            scores.append(tmp1)
            continue
        for i2 in range(6):
            tmp2 = tmp1 + dice[combi[1]][i2]
            if n == 2:
                scores.append(tmp2)
                continue
            for i3 in range(6):
                tmp3 = tmp2 + dice[combi[2]][i3]
                if n == 3:
                    scores.append(tmp3)
                    continue
                for i4 in range(6):
                    tmp4 = tmp3 + dice[combi[3]][i4]
                    if n == 4:
                        scores.append(tmp4)
                        continue
                    for i5 in range(6):
                        tmp5 = tmp4 + dice[combi[4]][i5]
                        if n == 5:
                            scores.append(tmp5)
    return scores


def solution(dice):
    n = len(dice)
    # A가 가져가는 주사위 조합들
    a_combis = list(combinations(range(n), n//2))
    
    max_combi = None
    max_cnt = 0
    for a_combi in a_combis:
        # B가 가져가는 주사위 조합
        b_combi = tuple(set(x for x in range(n)).difference(a_combi))
        # A가 a_combi대로 주사위를 선택했을 때, 점수를 저장
        a_scores = get_scores(dice, a_combi)
        # B가 b_combi대로 주사위를 선택했을 때, 점수를 저장
        b_scores = get_scores(dice, b_combi)

        # 오름차순으로 정렬된 a와 b의 점수들을 비교해서
        # a_combi 조합으로 b_combi 조합을 몇번 이길 수 있는지 검사
        a_scores.sort()
        b_scores.sort()
        # print("a_scores:", a_scores)
        # print("b_scores:", b_scores)
        # a가 b를 이기는 경우를 이분탐색으로 구한다
        tmp = 0
        for a_score in a_scores:
            left = 0 # b_scores의 왼쪽 인덱스
            right = len(b_scores) - 1 # b_scores의 오른쪽 인덱스
            while left <= right:
                mid = (left + right) // 2
                if a_score <= b_scores[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # a가 b를 이기는 경우는 left
            tmp += left

        if max_cnt < tmp:
            max_cnt = tmp
            max_combi = [x+1 for x in a_combi]
        

    return max_combi
        
                
inputs = [
    [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]],
    [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]],
    [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
]

results = [[1, 4], [2], [1, 3]]

for i in range(3):
    print(solution(inputs[i]) == results[i])
    print('=' * 40)