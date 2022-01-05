def solution(s):
    s_list = make_list(s)
    s_list = sort_by_length(s_list)
    answer = make_tuple(s_list)
    return answer


def make_list(s):
    s = s[1:-1]

    result = []
    while len(s) > 0:
        left_bracket = s.find('{')
        right_bracket = s.find('}')

        tmp_s = s[left_bracket:right_bracket+1]
        tmp_s = tmp_s.replace('{', '').replace('}', '')
        tmp_s = list(map(int, tmp_s.split(',')))
        result.append(tmp_s)

        s = s[right_bracket+1:]

    return result


def sort_by_length(s_list):
    result = [0]*(len(s_list))

    # 길이가 n인 inner list -> result[n-1]의 원소
    for i in range(len(s_list)):
        for inner in s_list:
            if len(inner) == i+1:
                result[i] = inner
                break
    return result


def make_tuple(s_list):
    # 길이순으로 정렬된 s_list를 인자로 받음

    result = [0 for i in range(len(s_list))]
    for i in range(len(s_list)):
        # base case -> 첫번째 원소
        if i == 0:
            result[i] = s_list[i][0]
        else:
            result[i] = (set(s_list[i]) - set(result[:i])).pop()

    return result


s = "{{123}}"
print(solution(s))
