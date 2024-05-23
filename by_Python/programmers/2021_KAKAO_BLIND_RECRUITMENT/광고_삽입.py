def get_second(hhmmss):
    second = 0
    tmp = list(map(int, hhmmss.split(":")))
    second += tmp[0] * 3600
    second += tmp[1] * 60
    second += tmp[2]
    return second

def get_hhmmss(second):
    hh = second // 3600
    second %= 3600
    mm = second // 60
    second %= 60
    
    if hh < 10:
        hh = '0' + str(hh)
    else:
        hh = str(hh)
    
    if mm < 10:
        mm = '0' + str(mm)
    else:
        mm = str(mm)
    
    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)
    
    return ":".join([hh, mm, second])

def solution(play_time, adv_time, logs):

    # 모든 시간을 초로 변경한다
    play_sec = get_second(play_time)
    adv_sec = get_second(adv_time)
    sec_logs = []
    for i in range(len(logs)):
        start_time, end_time = logs[i].split('-')
        start_time = get_second(start_time)
        end_time = get_second(end_time)
        sec_logs.append([start_time, end_time])
    
    # total_time[x] = x시각에 시작된 재생 구간의 개수 - x시각에 종료된 재생구간의 개수
    total_time = [0] * (play_sec + 1)
    for start_time, end_time in sec_logs:
        total_time[start_time] += 1
        total_time[end_time] -= 1
    
    # total_time[x] = 시각 x부터 x+1까지 1초간의 구간을 포함하는 재생 구간의 개수
    for i in range(1, play_sec + 1):
        total_time[i] += total_time[i-1]

    # total_time[x] = 시각 0부터 (x+1)초까지, (x+1)초간의 구간을 포함하는 누적 재생시간
    for i in range(1, play_sec + 1):
        total_time[i] += total_time[i-1]
    
    # (i- adv_time + 1)에 광고를 넣을 때의 누적 재생시간을 구하여
    # 그 중에서 가장 긴 시간을 max_time에 저장한다.
    # max_time 값이 마지막으로 업데이트 될 떄의 시각 i - adv_time + 1을 문제에서 원하는 형태로 변환한 값이 문제에서 요구한 정답
    max_time = 0
    answer = 0
    for i in range(adv_sec - 1, play_sec):
        if i >= adv_sec:
            tmp = total_time[i] - total_time[i - adv_sec]
            if max_time < tmp:
                max_time = tmp
                answer = i - adv_sec + 1
        else:
            if max_time < total_time[i]:
                max_time = total_time[i]
                answer = i - adv_sec + 1
    
    print(get_hhmmss(answer))
    return get_hhmmss(answer)




play_time = ["02:03:55", "99:59:59", "50:00:00"]
adv_time = ["00:14:15", "25:00:00", "50:00:00"]
logs = [ 
    ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],
    ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],
    ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	
    ]
result = ["01:30:59", "01:00:00", "00:00:00"]

for i in range(len(result)):
    print(solution(play_time[i], adv_time[i], logs[i]) == result[i])
    print('-' * 30)