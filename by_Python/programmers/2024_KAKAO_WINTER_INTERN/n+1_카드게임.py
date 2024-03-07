# https://codingjj.tistory.com/112 참고

def solution(coin, cards):
    n = max(cards)
    goal = n + 1
    card_idx = n // 3
    round = 1
    combi = 0 # 현재 라운드에서 내가 더해서 낼 수 있는 카드 조합의 수
    special = 0 # 코인을 2개 사용해서 goal이 만들어지는 특별한 경우

    # 핸드에서 만들 수 있는지 확인한다
    for i in range(card_idx - 1):
        for j in range(i+1, card_idx):
            if cards[i] + cards[j] == goal:
                combi += 1 # 카드를 뽑지 않고 핸드로만 goal을 구성하는 경우는 1라운드밖에 없다!
                break
    
    for i in range(card_idx, n, 2):
        # cards[i], cards[i+1] -> 이번 턴에 뽑히는 카드
        for j in range(i):
            # 코인 1개 소모: cards[j]가 핸드에 포함되는 카드인 경우
            if j < card_idx:
                if cards[i] + cards[j] == goal and coin >= 1:
                    combi += 1
                    coin -= 1
                if cards[i+1] + cards[j] == goal and coin >= 1:
                    combi += 1
                    coin -= 1
            # 코인 2개 소모: cards[j]가 핸드에 포함되지 않는 카드인 경우
            else:
                if cards[i] + cards[j] == goal:
                    special += 1
                if cards[i+1] + cards[j] == goal:
                    special += 1
        # === 예외 처리 ===
        # 코인 2개 소모: 이번 턴에 뽑히는 카드 두개의 합이 goal
        if cards[i] + cards[i+1] == goal:
            special += 1
        
        if combi > 0:
            # combi를 저장해두고 round로 바꿔먹는 느낌
            round += 1
            combi -= 1 
        else: # 현재 라운드에서 낼 수 있는 카드 조합의 수가 0인 경우 special case를 확인한다
            if special > 0 and coin >= 2:
                special -= 1
                round += 1
                coin -= 2
            else:
                break
    return round
coins = [4, 3, 2, 10, 0]
cards_ = [
    [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]	,
    [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]	,
    [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]	,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    [1, 2, 3, 4, 5, 6]
]
results = [5, 2, 4, 1, 1]

for i in range(len(coins)):
    ret = solution(coins[i], cards_[i])
    print('#', i+1, results[i] == ret)
    if results[i] != ret:
        print("정답:", results[i])
        print("구한 답:", ret)
    print('-' * 40)