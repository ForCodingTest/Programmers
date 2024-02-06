from collections import deque
import math
def solution(cap, n, deliveries, pickups):
    answer = 0
    dq=deque([])
    deldq=deque([])
    pickdq=deque([])
    
    newAry=[]
    for idx,pac in enumerate(zip(deliveries[::-1],pickups[::-1])):
        if pac!=(0,0):
            dq.append([len(deliveries)-idx,*pac])
    
    for idx,deli in enumerate(deliveries[::-1]):
        deldq.append([len(deliveries)-idx,deli])
    for idx,pick in enumerate(pickups[::-1]):
        pickdq.append([len(deliveries)-idx,pick])
    
    # print(pickdq,deldq)
    while True:
        # print(dq)
        if len(pickdq)!=0 and pickdq[0][1]==0:
            pickdq.popleft()
        elif len(deldq)!=0 and deldq[0][1]==0:
            deldq.popleft()
        else:
            if pickdq and deldq:
                if pickdq[0][0]>deldq[0][0]:
                    fast=pickdq[0][1]
                    score=pickdq[0][0]
                elif pickdq[0][0]<deldq[0][0]:
                    fast=deldq[0][1]
                    score=deldq[0][0]
                else:
                    fast=max(pickdq[0][1],deldq[0][1])
                    score=pickdq[0][0]
            elif pickdq:
                fast=pickdq[0][1]
                score=pickdq[0][0]
            else:
                fast=deldq[0][1]
                score=deldq[0][0]
            # fast=1
            fastcap=math.ceil(fast/cap)*cap
            answer+=score*(math.ceil(fast/cap))*2
            # print(pickdq,deldq,answer)  
            truck(pickdq,deldq,fastcap)
        if len(pickdq)==0 and len(deldq)==0:
            break
    # for i in range(len(dq)):
    #     truck(dq,500000)
        
    return answer

def truck(pickdq,deldq,cap):
    delcap=cap
    pickcap=cap
    for i in range(len(deldq)):
        if deldq[i][1]>=delcap:
            deldq[i][1]-=delcap
            delcap=0
            break
        else:
            delcap-=deldq[i][1]
            deldq[i][1]=0  
            
    for i in range(len(pickdq)):
        if pickdq[i][1]>=pickcap:
            pickdq[i][1]-=pickcap
            pickcap=0
            break
        else:
            pickcap-=pickdq[i][1]
            pickdq[i][1]=0
        
            

# 10:02
# 10:34 80퍼 성공
# 치킨 먹으면서 12:37분 성공

# 1. 각 집에 배달 및 수거할 때, 원하는 개수만큼 택배를 배달 및 수거할 수 있습니다.

# 1. deliver와 pickup으로 끝에서 부터 보기
# 2. 0이 될때 까지 더하기