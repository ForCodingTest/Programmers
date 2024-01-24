import math
def solution(fees, records):
    answer = []
    dic={}
    answerdic={}
    Atime,Afee,perT,perF=fees
    for record in records:
        timeIn,num,op=record.split()
        if num not in dic:
            dic[num]=[transTime(timeIn),op]
            if num not in answerdic:
                answerdic[num]=0
        else:
            if dic[num][1]=="IN":
                answerdic[num]+=transTime(timeIn)-dic[num][0] 
                dic[num][1]=op
            else:
                dic[num]=[transTime(timeIn),op]
    for i in dic:
        if dic[i][1]=="IN":
            answerdic[i]+=transTime("23:59")-dic[i][0]
            
    for _,time in (sorted(answerdic.items())):
        if time<=Atime:
            answer.append(Afee)
        else:
            answer.append(Afee+math.ceil((time-Atime)/perT)*perF)
            
    return answer

def transTime(time):
    h,m=map(int,time.split(":"))
    return h*60+m

# 1. 주차요금계산

# 1. 입차후 출차내역 없으면 23:59출차로 간주
# 2. 누적
# 3. 기본시간 이하라면 기본요금 
# 4. 초과하면 기본요금+ 단위 시간 마다 단위요금
# 5. 단위 시간으로 나누어 떨어지지않으면 올림
# 6. a보다 작지 않은 최소의 정수

# 1. 누적 주차 시간 구하기
# 2. 차 번호별로 딕셔너리 만들기
#11시 21분
#12시 10분
