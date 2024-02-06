# 38분 소요

def solution(n, t, m, timetable):
    start = 9 * 60
    bus = [[start + (t * i)] for i in range(n)]    # bus[i]: i번째 버스의 [출발시간, 탑승크루의도착시간1, 탑승크루의도착시간2, ..., 탑승크루의도착시간j] - j는 최대 m
    timetable = sorted(list(map(get_minute, timetable)))
    i = 0
    for arrive in timetable:  # 버스 태우기
        while i < n:
            if bus[i][0] >= arrive and len(bus[i]) < m + 1:   # 버스보다 먼저 왔고 버스에 자리가 있으면 태우기 위해 break
                break
            i += 1
            
        if i < n:
            bus[i].append(arrive)
        else:
            break
    
    if len(bus[-1]) < m + 1:  # 마지막 버스에 빈 자리 있으면 도착 시간에 도착
        return get_time(bus[-1][0])
    if len(bus[-1]) >= m + 1: # 마지막 버스에 자리 없으면 마지막으로 탄 크루보다 1분 빨리 도착
        return get_time(bus[-1][-1] - 1)


def get_minute(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def get_time(minute):
    h = minute // 60
    m = minute % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2)

# zfill 오랜만이다
