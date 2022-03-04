def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1 = 0
    score2 = 0
    score3 = 0

    for i in range(len(answers)):
        idx1 = i % 5
        idx2 = i % 8
        idx3 = i % 10
        if answers[i] == student1[idx1]:
            score1 += 1
        if answers[i] == student2[idx2]:
            score2 += 1
        if answers[i] == student3[idx3]:
            score3 += 1

    max_score = score1
    max_students = [1]

    if score2 > max_score:
        max_score = score2
        max_students = [2]
    elif score2 == max_score:
        max_students.append(2)

    if score3 > max_score:
        max_score = score3
        max_students = [3]
    elif score3 == max_score:
        max_students.append(3)

    return max_students


print(solution([1, 3, 2, 4, 2]))
