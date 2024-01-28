from collections import deque

posiSet=((0,1),(1,0),(0,-1),(-1,0))
def solution(places):
    answer = []
    
    for idx,place in enumerate(places):
            check=[[False]*5 for _ in range(5)]
            for i in range(5):
                keep=False
                for j in range(5):
                    if place[i][j]=="P":
                        check[i][j]=True
                        if find((i,j),place,check)==False:
                            answer.append(0)
                            break
                else:
                    keep=True
                if keep==False:
                    break
            else:
                answer.append(1)
    return answer

def find(posi,place,check):
    dq=deque([])
    dq.append(posi)
    T=0
    while dq:
        if T>=2:
            break
        T+=1
        for _ in range(len(dq)):  
            R,C=dq.popleft()
            for addr,addc in posiSet:
                curr=R+addr
                curc=C+addc
                if 0<=curr<5 and 0<=curc<5:
                    if check[curr][curc]==False and place[curr][curc]=="P":
                        return False
                    if check[curr][curc]==False and place[curr][curc]=="O":
                        check[curr][curc]=True
                        dq.append((curr,curc))
    return True
    
    
        
    
    
    
    

# 6:35
# 7:02 분 정답률 76퍼
# 7:26 
# 1. 실수 : return 탭 위치 실수<<진짜 슬프네
# 2. 테스트케이스 잘못박아놨음

# 1.대기실은 5개이며, 각 대기실은 5x5 크기
# 2. 거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
# 3. 파티션으로 막혀 있을 경우에는 허용

# 1. 맨해튼거리 경우의 수 1+3+4+3+1 셋으로 다보기
# 2. 있으면 지키지 않음
# 3. 없으면 지킴