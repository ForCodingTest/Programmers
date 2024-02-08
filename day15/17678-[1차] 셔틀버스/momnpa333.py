from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable=sorted(timetable)
    time='09:00'
    dq=deque(timetable)
    busAry=[]
    for i in range(n-1):
        time=addtime(t*i)
        busAry.append(haveSeat(dq,m,time))
    dqc=dq.copy()
    if haveSeat(dq,m,addtime(t*(n-1))):
        return str(addtime(t*(n-1))//60).zfill(2)+":"+str(addtime(t*(n-1))%60).zfill(2)
    else:
        ans=findTime(dqc,m,addtime(t*(n-1)))
        return str(ans//60).zfill(2)+":"+str(ans%60).zfill(2)
        
    return answer
def haveSeat(dq,m,time):
    for i in range(m):
        H,M=map(int,dq[0].split(":"))
        crueT=H*60+M
        if crueT<=time:
            dq.popleft()
            m-=1
        if len(dq)==0:
            if m==0:
                return False
            else:
                return True
    if m>0:
        return True
    return False
        
#     else:
#         return False
def addtime(time):
    return 9*60+time
def findTime(dq,m,time):
    H,M=map(int,dq[0].split(":"))
    prevT=H*60+M
    firstT=prevT
    for i in range(m):
        H,M=map(int,dq[0].split(":"))
        crueT=H*60+M
        if crueT<=time:
            dq.popleft()
            m-=1
            if prevT!=crueT:
                prevT=crueT
        if len(dq)==0 or m==0:
            if firstT==prevT:
                return prevT-1
            return prevT-1
        
    
        

# 3:23
# 4:06
# 셔틀은 09:00부터 총 n회 t분 간격으로 역에 도착하며, 하나의 셔틀에는 최대 m명의 승객이 탈 수 있다.
# 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발한다. 예를 들어 09:00에 도착한 셔틀은 자리가 있다면 09:00에 줄을 선 크루도 탈 수 있다.
# 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각
# 도착한 크루 중 대기열에서 제일 뒤에 선다. 또한, 모든 크루는 잠을 자야 하므로 23:59에 집에 돌아간다. 따라서 어떤 크루도 다음날 셔틀을 타는 일은 없다.

# 1. 9시 출발
# 2. 가장 늦게 오는 버스
# 3. timetable 에서 자리가 있는지
# 4. 시간별로 손님을 태우고 pop하기
# 5. 마지막버스 마지막 손님으로 태우기
