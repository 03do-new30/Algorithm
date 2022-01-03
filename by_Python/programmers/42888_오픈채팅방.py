# 유저아이디:닉네임 정보 유지
user = dict()


def solution(record):
    answer = []

    for rec in record:
        rec_data = rec.split()

        cmd = rec_data[0]
        user_id = rec_data[1]
        if cmd == "Leave":
            answer.append((cmd, user_id))
        else:
            # 닉네임
            user_name = rec_data[2]
            # 유저 정보
            user[user_id] = user_name

            if cmd == "Enter":
                answer.append((cmd, user_id))

    # 결국, 최종 업데이트된 닉네임으로 출력해줘야 함
    for i in range(len(answer)):
        answer[i] = make_msg(answer[i][0], answer[i][1])

    return answer


def make_msg(cmd, user_id):
    if cmd == "Leave":
        return user[user_id] + "님이 나갔습니다."
    elif cmd == "Enter":
        return user[user_id] + "님이 들어왔습니다."


"""
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
"""
