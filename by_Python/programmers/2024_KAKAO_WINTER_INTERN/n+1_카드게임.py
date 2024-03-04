max_round = 0 # 최대 라운드를 저장할 글로벌 변수

# 현재 핸드에서 카드 두장을 내어 goal을 만들 수 있는가?
# 가능한 카드 쌍들을 반환한다
def check_goal(hands, goal):
    ret = []
    for i in range(len(hands) - 1):
        for j in range(i+1, len(hands)):
            if hands[i] + hands[j] == goal:
                ret.append((hands[i], hands[j]))
    return ret

def solve(hands, cards, coin, round, goal):
    global max_round

    # 종료 조건 1: 더이상 추가할 카드가 없을 때
    if len(cards) == 0:
        if round > max_round:
            max_round = round
        return
    
    # CASE 1: 카드를 추가하지 않는 경우
    pairs = check_goal(hands, goal)
    if len(pairs) > 0: # goal을 만들 수 있는 경우
        # 각각의 쌍을 없애가면서 다음 단계 진행
        for pair in pairs:
            tmp = list(set(hands).difference(pair))
            solve(tmp, cards[2:], coin, round + 1, goal)
    
    # CASE 2: 카드를 두개 다 추가하는 경우
    if coin >= 2:
        new_hands = hands + cards[:2]
        pairs = check_goal(new_hands, goal)
        if len(pairs) > 0: # goal을 만들 수 있는 경우
            for pair in pairs:
                tmp = list(set(new_hands).difference(pair))
                solve(tmp, cards[2:], coin-2, round+1, goal)
    # CASE 3: 카드를 한개만 추가하는 경우
    if coin >= 1:
        # CASE 3-1: 첫번째 카드만 추가하는 경우
        new_hands = hands + [cards[0]]
        pairs = check_goal(new_hands, goal)
        if len(pairs) > 0:
            for pair in pairs:
                tmp = list(set(new_hands).difference(pair))
                solve(tmp, cards[2:], coin-1, round+1, goal)
        # CASE 3-2: 두번째 카드만 추가하는 경우
        new_hands = hands + [cards[1]]
        pairs = check_goal(new_hands, goal)
        if len(pairs) > 0:
            for pair in pairs:
                tmp = list(set(new_hands).difference(pair))
                solve(tmp, cards[2:], coin-1, round+1, goal)
    
    if round > max_round:
        max_round = round

def solution(coin, cards):
    global max_round
    max_round = 0 # 글로벌 변수 초기화
    n = max(cards)
    hands = cards[:n//3]
    cards = cards[n//3:]
    solve(hands, cards, coin, 1, n+1)
    return max_round

coins = [4, 3, 2, 10]
cards_ = [
    [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]	,
    [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]	,
    [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]	,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]	
]
results = [5, 2, 4, 1]

for i in range(4):
    print(results[i] == solution(coins[i], cards_[i]))
    print('-' * 40)