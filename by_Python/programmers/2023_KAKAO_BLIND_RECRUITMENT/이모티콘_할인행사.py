from itertools import product

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    
    # 이모티콘의 할인율 경우들을 구함
    cases = product((10, 20, 30, 40), repeat = m)
    
    results = []

    # 할인율 조합 케이스별로 소비자의 구매 방식을 탐색
    for case in cases:
        members = 0 # 서비스에 가입한 사람 수
        income = 0 # 총 수입
        for i in range(n):
            percent, budget = users[i] # 소비자 i의 구매 결정 할인율, 최대 지불 비용
            spent = 0 # 소비자 i가 지금까지 지불한 비용
            join = False # 소비자 i의 서비스 가입 여부
            
            for j in range(m):
                sale_percent = case[j] # 이모티콘의 할인율
                if sale_percent < percent:
                    continue
                price = emoticons[j] - emoticons[j] * sale_percent * 0.01 # 이모티콘 구매가
                spent += price
                # 최대 지불 비용 이상인지 검사
                if spent >= budget:
                    join = True
                    break
            
            if join:
                # 이모티콘 서비스에 가입
                members += 1
            else:
                income += spent
        
        # 검사한 case의 멤버 수와 총 수입을 results에 저장
        results.append([members, income])
    
    results.sort(key = lambda x : (-x[0], -x[1]))
    return results[0]

users = [
    [[40, 10000], [25, 10000]],
    [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
]
emoticons = [
    [7000, 9000],
    [1300, 1500, 1600, 4900]
    ]
result = [
    [1, 5400],
    [4, 13860]
]
for i in range(2):
    print(solution(users[i], emoticons[i]) == result[i])
    print('-' * 40)