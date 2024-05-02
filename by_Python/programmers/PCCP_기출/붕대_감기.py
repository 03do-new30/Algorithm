def solution(bandage, health, attacks):
    answer = 0
    # 마지막 공격 시간
    last_attack = attacks[-1][0]
    damages = [0] * (last_attack + 1)
    for attack_time, damage in attacks:
        damages[attack_time] = damage
    

    max_bandage, heal, bonus_heal = bandage
    band_time = 0
    hp = health

    for time in range(1, last_attack + 1):
        # 공격 여부 검사
        if damages[time] > 0:
            hp -= damages[time]
            if hp <= 0:
                answer = -1
                break
            band_time = 0
            continue
        # 붕대 감기
        band_time += 1
        if band_time == max_bandage:
            next_hp = hp + heal + bonus_heal
            band_time = 0
        else:
            next_hp = hp + heal
        
        if next_hp > health:
            hp = health
        else:
            hp = next_hp
    if answer == -1:
        return answer
    return hp

bandage = [
    [5, 1, 5], [3, 2, 7], [4, 2, 7], [1, 1, 1]
]
health = [30, 20, 20, 5]
attacks = [
    [[2, 10], [9, 15], [10, 5], [11, 5]]	,
    [[1, 15], [5, 16], [8, 6]]	,
    [[1, 15], [5, 16], [8, 6]]	,
    [[1, 2], [3, 2]]	
]
result = [5, -1, -1, 3]

for i in range(len(result)):
    print(solution(bandage[i], health[i], attacks[i]) == result[i])