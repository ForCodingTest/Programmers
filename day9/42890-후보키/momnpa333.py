from itertools import combinations

def solution(relation):
    answer = set()
    L=len(relation[0])
    
    #relation = [i for i in zip(*relation)]
    
    for i in range(L):
        for combiset in combinations(range(L),i+1):
            if isFK(combiset,relation):
                if isposi(combiset,answer):
                    answer.add(combiset)
                #pass
            # answer.add()
    return len(answer)
def isFK(combi,relation):
    rowset=[]
    for entity in relation:
        entityset=[]
        for idx in combi:
            entityset.append(entity[idx])
        if entityset in rowset:
            return False
        rowset.append(entityset)
    return True

def isposi(combiset,answer):
    for ans in answer:
         if len(set(ans)-set(combiset))==0:
                return False
    return True
    
# 10:00
# 10:25

# 1. 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 2. 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다

# 1. 0,1,2,3 01,02,03, combintion 사용
# 2. zip으로 row col 바꾸기