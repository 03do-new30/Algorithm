from collections import deque
def solution(lottos, win_nums):
    answer = []
    # win_nums를 dict로 바꿔본다
    win_dict = dict()
    for num in win_nums:
        if num in win_dict:
            win_dict[num] += 1
        else:
            win_dict[num] = 1
    # 현재까지 일치하는 번호
    current_match = 0
    # 0의 개수
    zero_count = 0
    for num in lottos:
        if num == 0:
            zero_count += 1
            continue
        if num in win_dict and win_dict[num] > 0:
            win_dict[num] -= 1
            current_match += 1
    # 최고 순위
    best_match = current_match + zero_count
    # 최저 순위
    worst_match = current_match
    
    return [rank(best_match), rank(worst_match)]

def rank(match):
    if match >= 2:
        return 7 - match
    else:
        return 6

lottos = [[44, 1, 0, 0, 31, 25], [0, 0, 0, 0, 0, 0], [45, 4, 35, 20, 3, 9]]
win_nums = [
    [31, 10, 45, 1, 6, 19],
    [38, 19, 20, 40, 15, 25],
    [20, 9, 3, 45, 4, 35]
]
result = [[3, 5], [1, 6], [1, 1]]
for i in range(len(result)):
    print(solution(lottos[i], win_nums[i]) == result[i])