def solution(numbers, hand):
    answer = ''

    # 초기 왼손, 오른손 위치
    L = "*"
    R = "#"

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            L = number
        elif number in [3, 6, 9]:
            answer += "R"
            R = number
        else:
            L_dist = get_dist(L, number)
            R_dist = get_dist(R, number)
            if L_dist < R_dist:
                L = number
                answer += "L"
            elif L_dist > R_dist:
                R = number
                answer += "R"
            else:
                if hand == "left":
                    L = number
                    answer += "L"
                else:
                    R = number
                    answer += "R"

    return answer


def get_row(n):
    if n in [1, 2, 3]:
        return 1
    elif n in [4, 5, 6]:
        return 2
    elif n in [7, 8, 9]:
        return 3
    else:
        return 4


def get_col(n):
    if n in [1, 4, 7, "*"]:
        return 1
    elif n in [2, 5, 8, 0]:
        return 2
    else:
        3


def get_dist(curr, next):
    if get_col(curr) == get_col(next):
        return abs(get_row(curr) - get_row(next))
    else:
        return abs(get_row(curr) - get_row(next)) + 1


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))
