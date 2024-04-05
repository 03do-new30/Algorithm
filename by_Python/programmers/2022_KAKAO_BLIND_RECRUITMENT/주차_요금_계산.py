from collections import defaultdict
from math import ceil

def get_minutes(start, end):
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    start_minutes = 60 * start_h + start_m
    end_minutes = 60 * end_h + end_m
    return end_minutes - start_minutes

def get_fee(time, fees):
    basic_min, basic_fee, unit_min, unit_fee = fees
    if time <= basic_min:
        return basic_fee
    return basic_fee + ceil((time - basic_min) / unit_min) * unit_fee

def solution(fees, records):
    parked = set()
    car_in = dict() # 차량 입차 시간 저장
    car_time = defaultdict(int) # 차량 별 총 주차시간 저장
    for record in records:
        time_log, car_id, status = record.split()
        car_id = int(car_id)
        if status == "IN":
            parked.add(car_id)
            car_in[car_id] = time_log
        else:
            start_time = car_in[car_id]
            parked_time = get_minutes(start_time, time_log)
            # print("{0}번 차량 주차되어 있던 시간: {1}".format(car_id, parked_time))
            car_time[car_id] += parked_time
            parked.remove(car_id)
    # 아직 parked에 남아있는 차가 있다면 23:59 출차로 처리
    if parked:
        for left_car in parked:
            car_time[left_car] += get_minutes(car_in[left_car], "23:59")

    answer = []
    for car_id in sorted(car_time.keys()):
        answer.append(get_fee(car_time[car_id], fees))

    return answer

fees = [
    [180, 5000, 10, 600],
    [120, 0, 60, 591],
    [1, 461, 1, 10]
]
records =[
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],
    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"],
    ["00:00 1234 IN"]
]
result = [
    [14600, 34400, 5000],
    [0, 591],
    [14841]
]

for i in range(len(result)):
    print(solution(fees[i], records[i]) == result[i])
    print('-' * 40)