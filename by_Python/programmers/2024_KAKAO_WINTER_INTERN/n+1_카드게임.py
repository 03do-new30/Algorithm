def solution(coin, cards):
    n = max(cards)
    goal = n + 1
    hands = cards[:n//3] # 손에 든 카드
    cards = cards[n//3:] # 남아있는 카드
    discard = [] # 버림 더미
    round = 1 # 라운드 기록
    while True:
    #     print("#", round)
    #     print("hands:", hands)
    #     print("cards:", cards)
    #     print("버림더미:", discard)
    #     print("coin:", coin)
        # 이번 라운드에 뽑을 카드들 저장
        candidates = []
        if len(cards) >= 2:
            candidates = cards[:2]
        # print("candidates:", candidates)
        
        # 1. hands만으로 goal을 만들 수 있는가? (코인 0개 소모)
        done = False
        for hand in hands:
            if goal - hand in hands: # 통과
                # 핸드에서 goal을 만드는 숫자카드 쌍들 삭제
                hands.remove(hand)
                hands.remove(goal - hand)
                done = True
                break
        if done:
            # 이번 라운드에 쓰이지 않은 카드들을 버림 더미에 저장
            discard += candidates
            # 카드 더미 조정
            if len(cards) >= 2:
                cards = cards[2:]
            # 라운드 증가
            round += 1
            continue # 다음 라운드로
        
        if coin < 1:
            return round
        
        # 2. hands의 카드와 candidates의 카드를 합쳐서 goal을 만들 수 있는가? (코인 1개 소모)
        if coin >= 1:
            for hand in hands:
                if goal - hand in candidates: # 통과
                    # 핸드와 뽑힌 카드에서 goal을 만드는 숫자카드 쌍 삭제
                    hands.remove(hand)
                    candidates.remove(goal - hand)
                    done = True
                    break
        if done:
            # 이번 라운드에 쓰이지 않은 카드들을 버림 더미에 저장
            discard += candidates
            # 카드 더미 조정
            if len(cards) >= 2:
                cards = cards[2:]
            # 라운드 증가
            round += 1
            # 코인 감소
            coin -= 1
            continue # 다음 라운드로


        
        # 3. hands와 버림더미로 goal을 만들 수 있는가? (코인 1개 소모)
        if len(hands) > 0 and len(discard) > 0 and coin >= 1:
            for hand in hands:
                if goal - hand in discard:
                    # 핸드와 버림더미에서 goal을 만드는 쌍 삭제
                    hands.remove(hand)
                    discard.remove(goal - hand)
                    done = True
                    break

        if done:
            # 이번 라운드에 쓰이지 않은 카드들을 버림 더미에 저장
            discard += candidates
            # 카드 더미 조정
            if len(cards) >= 2:
                cards = cards[2:]
            # 라운드 증가
            round += 1
            # 코인 감소
            coin -= 1
            continue # 다음 라운드로

        # 4. candidates만으로 goal을 만들 수 있는가? (코인 2개 소모)
        if len(candidates) >= 2 and coin >= 2:
            if sum(candidates) == goal:
                # 카드 더미 조정
                if len(cards) >= 2:
                    cards = cards[2:]
                # 라운드 증가
                round += 1
                # 코인 감소
                coin -= 2
                # 다음 라운드로
                continue

        if coin < 2:
            return round
        
        # 5. candidates와 버림더미로 goal을 만들 수 있는가? (코인 2개 소모)
        if len(candidates) > 0 and len(discard) > 0 and coin >= 2:
            for candidate in candidates:
                if goal - candidate in discard:
                    # candidate와 버림더미에서 goal을 만드는 쌍 삭제
                    candidates.remove(candidate)
                    discard.remove(goal - candidate)
                    done = True
                    break
        if done:
            # 이번 라운드에 쓰이지 않은 카드들을 버림 더미에 저장
            discard += candidates
            # 카드 더미 조정
            if len(cards) >= 2:
                cards = cards[2:]
            # 라운드 증가
            round += 1
            # 코인 감소
            coin -= 2
            continue # 다음 라운드로

        # 6. 버림더미만으로 goal을 만들 수 있는가? (coin 2개 소모)
        if len(discard) >= 2 and coin >= 2:
            for d in discard:
                if goal - d in discard:
                    discard.remove(d)
                    discard.remove(goal - d)
                    done = True
                    break
        if done:
            # 카드 더미 조정
            if len(cards) >= 2:
                cards = cards[2:]
            # 라운드 증가
            round += 1
            # 코인 감소
            coin -= 2
            continue # 다음 라운드로
        
        # 여기까지 오면 더이상 라운드 진행할 수 없음
        break
    return round

coins = [4, 3, 2, 10, 1, 8, 3, 4, 1, 4]
cards_ = [
    [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]	,
    [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]	,
    [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]	,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    [6, 2, 1, 4, 5, 3],
    [1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6, 7],
    [5, 4, 3, 2, 1, 6],
    [1, 12, 2, 11, 3, 10, 4, 9, 5, 6, 7, 8],
    [1, 12, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [1, 6, 2, 5, 3, 4],
]
results = [5, 2, 4, 1, 2, 7, 3, 5, 2, 4]

for i in range(len(coins)):
    print('#', i+1, results[i] == solution(coins[i], cards_[i]))
    print('-' * 40)