from bisect import bisect_left
from itertools import combinations

def solution(infos, query):
    answer = []
    # 조건들을 이용하여 특성 조합을 키로 갖는 딕셔너리를 만든다
    combi_dict = dict()
    
    # combi_dict[언어+직군+경력+음식] = [해당조건을 만족하는 지원자 1의 점수, 해당조건을 만족하는 지원자 2의 점수, ...]
    for info in infos:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])

        for i in range(5):
            wild_card_indices = list(combinations([0, 1, 2, 3], i))
            for wild_card_index in wild_card_indices:
                tmp = condition[:]
                for index in wild_card_index:
                    tmp[index] = '-'
                key = ''.join(tmp)
                if key in combi_dict:
                    combi_dict[key].append(score)
                else:
                    combi_dict[key] = [score]

    # 점수 이분 탐색을 위한 정렬
    for scores in combi_dict.values():
        scores.sort()

    for q in query:
        tmp = q.split(' ')
        while 'and' in tmp:
            tmp.remove('and')
        target_score = int(tmp[4])
        q_key = ''.join(tmp[:4])
        
        # combi_dict[q_key]에서 target_score 이상인 점수의 개수를 구한다
        # 이분탐색을 위해서 정렬한다
        count = 0
        if q_key in combi_dict:
            data = combi_dict[q_key]
            idx = bisect_left(data, target_score)
            count = len(data) - idx
        answer.append(count)
    
    return answer

info = [["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]	]
query = [["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]	]
result = [[1,1,1,1,2,4]]
for i in range(len(result)):
    print(solution(info[i], query[i]) == result[i])
    print('-' * 30)
