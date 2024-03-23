def solution(survey, choices):
    metric_rt = {'R':0, 'T':0}
    metric_cf = {'C':0, 'F':0}
    metric_jm = {'J':0, 'M':0}
    metric_an = {'A':0, 'N':0}
    metrics = [metric_rt, metric_cf, metric_jm, metric_an]

    n = len(survey)
    for i in range(n):
        type_idx = 0
        if 'R' in survey[i]:
            type_idx = 0
        elif 'C' in survey[i]:
            type_idx = 1
        elif 'J' in survey[i]:
            type_idx = 2
        elif 'A' in survey[i]:
            type_idx = 3
        
        choice = choices[i]
        disagree_type = survey[i][0]
        agree_type = survey[i][1]
        if choice < 4:
            metrics[type_idx][disagree_type] += 4 - choice
        elif choice > 4:
            metrics[type_idx][agree_type] += choice - 4


    answer = ''

    if metric_rt['R'] >= metric_rt['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if metric_cf['C'] >= metric_cf['F']:
        answer += 'C'
    else:
        answer += 'F'

    if metric_jm['J'] >= metric_jm['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if metric_an['A'] >= metric_an['N']:
        answer += 'A'
    else:
        answer += 'N'
    
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