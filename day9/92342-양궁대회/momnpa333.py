from itertools import combinations_with_replacement

def solution(n, info):
    
    answer = [0,[0]*11]
    answer1=[]
    for targets in combinations_with_replacement(range(11),n):
        Rinfo=[0]*11
        for target in targets:
            Rinfo[target]+=1
        score=getscore(info,Rinfo)
        if score>answer[0]:
            answer=[score,Rinfo]
        if score==answer[0] and morelow(answer[1],Rinfo):
            answer=[score,Rinfo]
    if answer[0]>0:
        return answer[1]
    return [-1]
def getscore(info,Rinfo):
    Ascore=0
    Rscore=0

    for idx,target in enumerate(zip(info,Rinfo)):
        A,R=target
        score=10-idx
        if A==R==0:
            continue
        if A>=R:
            Ascore+=score
        else:
            Rscore+=score
    # if (Rinfo==[1,1,2,0,1,2,2,0,0,0,0] or Rinfo==[1,1,2,0,1,0,0,0,0,0,4]):
    #     print(Rscore-Ascore,Rinfo)
    if Rscore-Ascore>0:
        return Rscore-Ascore
    else:
        return -1
    
def morelow(info,Rinfo):
    for i,R in zip(info[::-1],Rinfo[::-1]):
        if i==R:
            continue
        if i<R:
            return True
        else:
            return False
# 10:26
# 10:57 
# 1. 어피치가 화살 n발을 다 쏜 후에 라이언이 화살 n발을 쏩니다.
# 2. 과녁판은 아래 사진처럼 생겼으며 가장 작은 원의 과녁 점수는 10점이고 가장 큰 원의 바깥쪽은 과녁 점수가 0점입
# 3. 만약, k(k는 1~10사이의 자연수)점을 어피치가 a발을 맞혔고 라이언이 b발을 맞혔을 경우 더 많은 화살을 k점에 맞힌 선수가 k 점을 가져갑니다. 단, a = b일 경우는 어피치가 k점을 가져갑니다. k점을 여러 발 맞혀도 k점 보다 많은 점수를 가져가는 게 아니고 k점만 가져가는 것을 유의하세요. 또한 a = b = 0 인 경우, 즉, 라이언과 어피치 모두 k점에 단 하나의 화살도 맞히지 못한 경우는 어느 누구도 k점을 가져가지 않습니다.
# 4. 라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.
# 5. 라이언이 우승할 수 없는 경우(무조건 지거나 비기는 경우)는 [-1]을 return
# 6. 라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.

# 1. product 사용 (10,10,10,10,10)~(0,0,0,0,0)
# 2. 과녁 별로 점수 측정
# 3. 가장 낮은 점수를 더많이 맞힌 경우

