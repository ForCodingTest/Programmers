# 24분 소요

import math

def solution(fees, records):
    total_times = {}
    in_time = {}
    for record in records:
        time, car, history = record.split(" ")
        if history == 'IN':
            in_time[car] = time
            if car not in total_times:
                total_times[car] = 0
        else:
            total_times[car] += get_time(in_time[car], time)
            del in_time[car]
    
    # 출차 기록이 없는 차량
    for car, time in in_time.items():
        total_times[car] += get_time(in_time[car], "23:59")
    
    # 요금 계산
    total_fees = {}
    for car, time in total_times.items():
        if total_times[car] > fees[0]:
            total_fees[car] = fees[1] + math.ceil((total_times[car] - fees[0]) / fees[2]) * fees[3]
        else:
            total_fees[car] = fees[1]
    
    _, answer = zip(*sorted(total_fees.items(), key = lambda x: x[0]))
    
    return answer


def get_time(i, o):
    return get_miniute(o) - get_miniute(i)
    
    
def get_miniute(time):
    h, m = time.split(":")
    return int(h) * 60 + int(m)
