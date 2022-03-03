def solution(id_list, report, k):
    # 아이디의 고유번호는 id_list에서의 인덱스값
    # id_dict = 문자열 id를 키로 가지고, 고유 번호를 value로 가짐
    id_dict = dict()
    # report_dict = 고유번호를 키로 가지고, 신고당한 횟수를 value로 가짐
    report_dict = dict()

    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
        report_dict[i] = 0

    # reported[i][j] = 유저i가 유저j를 신고하면 True, 아니면 False
    reported = [[False]*len(id_list) for _ in range(len(id_list))]

    for log in report:
        user1, user2 = log.split()
        user1 = id_dict[user1]
        user2 = id_dict[user2]

        if not reported[user1][user2]:
            reported[user1][user2] = True
            report_dict[user2] += 1

    # 각 유저가 받은 결과 메일 수
    answer = []
    for i in range(len(id_list)):
        mails = 0
        for j in range(len(id_list)):
            if reported[i][j] and report_dict[j] >= k:
                mails += 1
        answer.append(mails)

    return answer
