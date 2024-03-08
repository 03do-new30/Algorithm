cases = []

def get_cases(m, cnt, case):
    global cases
    if m == cnt:
        cases.append(case)
        return
    sales = [10, 20, 30, 40]
    for i in range(4):
        get_cases(m, cnt + 1, case + [sales[i]])

def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    results = [] # 가입자 수와 수입을 저장하는 리스트
    # cases: 이모티콘 별 할인율 조합들을 구함
    # global 변수 cases 사용 전 초기화
    global cases
    if len(cases) > 0:
        cases = []
    get_cases(m, 0, [])

    # emoticons 가격 높은 것부터 구매하게 정렬
    emoticons.sort(reverse = True)
    for case in cases:
        # 현재 케이스의 총 수입
        money = 0
        # 현재 케이스의 총 가입자 수
        members = 0
        # 유저별로 구매방식 탐색
        for i in range(n):
            # 구매 희망 비율, 최대 지불 가격
            hope_sale, max_spent = users[i]
            # users[i]가 현재까지 쓴 비용
            spent = 0
            # 이모티콘 서비스 가입 여부
            service = False
            for j in range(m):
                if case[j] < hope_sale: # 할인율 검사
                    continue

                price = emoticons[j] - emoticons[j] * case[j] * 0.01
                if spent + price >= max_spent:
                    service = True # 서비스 가입
                    break
                else:
                    spent += price
            if service:
                members += 1
            else:
                money += spent
        
        results.append([members, money])
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