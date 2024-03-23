def solution(survey, choices):
    scores = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for i in range(len(survey)):
        choice = choices[i]
        if choice < 4:
            scores[survey[i][0]] += 4 - choice
        elif choice > 4:
            scores[survey[i][1]] += choice - 4
    
    answer = ''
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"

    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"

    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer

survey = [
    ["AN", "CF", "MJ", "RT", "NA"],
    ["TR", "RT", "TR"]
]

choices = [
    [5, 3, 2, 7, 5]	,
    [7, 1, 3]
]

result = [
    "TCMA",
    "RCJA"
]

for i in range(len(result)):
    print(result[i] == solution(survey[i], choices[i]))
    print('-' * 40)