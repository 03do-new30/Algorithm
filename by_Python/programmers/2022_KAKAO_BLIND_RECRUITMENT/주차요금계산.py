import math
from collections import defaultdict

def get_parking_minute(entry, exit):
    entry_hour, entry_minute = map(int, entry.split(':'))
    exit_hour, exit_minute = map(int, exit.split(':'))
    
    tmp_minute = exit_minute - entry_minute
    tmp_hour = exit_hour - entry_hour
    
    if tmp_minute < 0:
        tmp_minute += 60
        tmp_hour -= 1
        
    return tmp_minute + tmp_hour * 60

def get_parking_fee(fees, parking_minute):
    
    basic_minute, basic_fee, extra_minute, extra_fee = fees
    
    if parking_minute < basic_minute:
        return basic_fee
    
    return basic_fee + math.ceil((parking_minute - basic_minute) / extra_minute) * extra_fee

def solution(fees, records):
    # 차 별 누적 시간
    total_minute = defaultdict(int)
    # 입차 로그
    entry_log = dict()
    # 누적 요금 로그
    total_fee = dict()
    
    for record in records:
        
        time, car_id, in_out = record.split()
        
        if in_out == "IN":
            entry_log[car_id] = time
        else:
            enter = entry_log[car_id]
            total_minute[car_id] += get_parking_minute(enter, time)
            # 입차 내역 삭제
            del entry_log[car_id]
    
    # 남아있는 입차내역 처리
    for car_id in entry_log:
        enter = entry_log[car_id]
        total_minute[car_id] += get_parking_minute(enter, "23:59")
    
    # 누적 주차 시간에 대하여 요금 적용
    answer = []
    
    car_ids = sorted(total_minute.keys())
    for car_id in car_ids:
        answer.append(get_parking_fee(fees, total_minute[car_id]))
    
    return answer