def solution(new_id):
    # 1단계
    answer = new_id.lower()
    answer = list(answer)
    # 2단계
    del_chars = []
    for i in range(len(answer)):
        if answer[i] in ('-', '_', '.') or answer[i].isalnum():
            continue
        del_chars.append(answer[i])
    for del_char in del_chars:
        answer.remove(del_char)
    # 3단계
    tmp_answer = []
    for i in range(len(answer)):
        if answer[i] != '.':
            tmp_answer.append(answer[i])
        else:
            if len(tmp_answer) > 0 and tmp_answer[-1] != '.':
                tmp_answer.append(answer[i])
    answer = tmp_answer
    # 4단계
    answer = ''.join(answer)
    answer = answer.strip('.')
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip('.')
    # 7단계
    if len(answer) <= 2:
        last_char = answer[-1]
        while len(answer) < 3:
            answer = answer + last_char
    
    return answer

new_id = ["...!@BaT#*..y.abcdefghijklm", "z-+.^.", "=.=", "123_.def", "abcdefghijklmn.p"]
result = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]
for i in range(len(result)):
    print(solution(new_id[i]) == result[i])
    print('-' * 30)