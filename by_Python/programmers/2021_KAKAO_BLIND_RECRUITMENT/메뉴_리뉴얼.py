from itertools import combinations

def solution(orders, course):
    answer = []

    for i in course:
        # print("단품메뉴", i, "개 조합")
        course_cnt = dict()
        for order in orders:
            order = sorted(list(order))
            combis = combinations(order, i)
            for combi in combis:
                if combi in course_cnt:
                    course_cnt[combi] += 1
                else:
                    course_cnt[combi] = 1
        # print("course_cnt:", course_cnt)
        if len(course_cnt) <= 0:
            continue
        max_cnt = max(course_cnt.values())
        if max_cnt < 2:
            continue
        for x in course_cnt:
            if course_cnt[x] == max_cnt:
                answer.append(''.join(x))
    
    answer.sort()
    # print("answer:", answer)
    return answer

orders = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],["XYZ", "XWY", "WXA"]]
course =[[2,3,4], [2,3,5], [2,3,4]]
result = [["AC", "ACDE", "BCFG", "CDE"],["ACD", "AD", "ADE", "CD", "XYZ"],["WX", "XY"]]

for i in range(len(result)):
    print(solution(orders[i], course[i]) == result[i])
    print('-' * 30)