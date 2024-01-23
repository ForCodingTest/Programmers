#임마 개오래걸려 시간 재는 거 포기함 40분이상은 걸린 거 같은데...
def solution(fees, records):
    #records["시간 번호 IN/OUT","","",..] 시간 HH:MM
    #answer[요금1,요금2,요금3] 단 차량번호가 작은 자동차 순서부터
    cars = {}
    #같은 차끼리 묶?
    for i in records:
        sp = i.split(" ")
        time = sp[0].split(":")
        int_time = int(time[0]) * 60 + int(time[1])
        if sp[1] in cars:
            cars[sp[1]].append(int_time)
        else:
            cars[sp[1]] = []
            cars[sp[1]].append(int_time)

    #당일 출차 X
    for num in cars.keys():
        if len(cars[num]) % 2 == 1:
            cars[num].append(23 * 60 + 59)

    
    #시간계산하기
    time = 0
    for i in cars.keys():
        for j in range(0,len(cars[i])-1,2):
            time += (cars[i][j+1] - cars[i][j])
        cars[i] = time
        time = 0
    #요금 계산하기
    #fees[기본시간,기본요금,단위시간,단위요금]
    for i in cars.keys():
        #기본요금
        if cars[i] <= fees[0]:
            cars[i] = fees[1]
        else:
            #계산
            time = cars[i] - fees[0]
            if time % fees[2] == 0:
                cars[i] = fees[1] + int(time/fees[2])*fees[3]
            else:
                cars[i] = fees[1] + int(time/fees[2]+1) * fees[3]
    # print(cars)
    answer = dict(sorted(cars.items()))
    return list(answer.values())
#출차 x -> 23:59분 출차로 간주
#요금 = 기본요금 + 올림((시간 - 기본 시간) / 단위시간) * 단위요금
