def solution(today, terms, privacies):
    
    today = list(map(int, today.split('.')))
    term_dict = dict()
    for term in terms:
        a, b = term.split(' ')
        term_dict[a] = int(b)
    
    answer = []
    for i in range(len(privacies)):
        date, code = privacies[i].split(' ')
        date = list(map(int, date.split('.')))
        date[1] += term_dict[code]
        while date[1] > 12:
            date[1] -= 12
            date[0] += 1
        
        if today[0] > date[0]: # Y 초과
            answer.append(i+1)
            continue
        elif today[0] == date[0]:
            if today[1] > date[1]: # M 초과
                answer.append(i+1)
                continue
            elif today[1] == date[1]:
                if today[2] >= date[2]: # D 유효기간에 걸림
                    answer.append(i+1)

    return answer

today_ = ["2022.05.19", "2020.01.01"]
terms_ = [["A 6", "B 12", "C 3"],
          ["Z 3", "D 5"]]
privacies_ = [
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
    ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
]
result_ = [[1, 3], [1, 4, 5]]

for i in range(2):
    print(solution(today_[i], terms_[i], privacies_[i]) == result_[i])
    print('-' * 40)