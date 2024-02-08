       
from collections import defaultdict,Counter

def solution(gems):
    answer = [100001,0,0]
    L=len(set(gems))
    
    cnt=defaultdict(int)
    right=0
    left=0
    flag=False
    while left<len(gems) and right<len(gems):
        for gem in gems[right:]:
            cnt[gem]+=1
            right+=1
            if len(cnt)==L:
                if right-left<answer[0]:
                    answer=[right-left,left+1,right]
                break
        for gem in gems[left:]:
            cnt[gem]-=1
            left+=1
            if cnt[gem]==0:
                del cnt[gem]
                break
            if len(cnt)==L:
                if right-left<answer[0]:
                    answer=[right-left,left+1,right]
            
            
    
    return answer[1:]


# 3:37
# 4:10 첫 solve 40퍼
# 4:50 두번째 46.7
# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
# 가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return 하도록 하며, 만약 가장 짧은 구간이 여러 개라면 시작 진열대 번호가 가장 작은 구간을 return 합니다.
# gems 배열의 크기는 1 이상 100,000 이하입니다

# 1. right로 새로운거 생길때 마다 right update 및 counter로 개수세기
# 2. left로 이동하는데 counter 0이 안될때 까지