from  collections import defaultdict
def solution(id_list, report, k):
    report_dict = defaultdict(set)
    for repo in report:
        a, b = repo.split()
        report_dict[a].add(b)
    
    # print("report_dict:", report_dict)

    count_dict = dict()
    for id in id_list:
        count_dict[id] = 0
    for report_log in report_dict.values():
        for name in report_log:
            count_dict[name] += 1
    # print("count_dict:", count_dict)

    banned = []
    for id in id_list:
        if count_dict[id] >= k:
            banned.append(id)
    # print("banned:", banned)

    noti = [0] * len(id_list)
    for i in range(len(id_list)):
        for banned_member in banned:
            if banned_member in report_dict[id_list[i]]:
                noti[i] += 1
    # print("noti:", noti)

    
    answer = noti
    return answer

id_list = [
    ["muzi", "frodo", "apeach", "neo"],
    ["con", "ryan"]
]
report = [
    ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
    ["ryan con", "ryan con", "ryan con", "ryan con"]
]
k = [2, 3]
result = [[2, 1, 1, 0], [0, 0]]

for i in range(len(result)):
    print(solution(id_list[i], report[i], k[i]) == result[i])
    print('-' * 40)