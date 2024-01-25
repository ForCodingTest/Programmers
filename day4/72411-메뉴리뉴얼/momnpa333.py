from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = {}
    answer1=[]
    for num in course:
        answer[num]=[]
    setMenu=[]
    countdic=Counter("")
    for num in course:
        for order in orders:
            for combi in combinations(order,num):
                combi=sorted(list(combi))
                #print(combi)
                setMenu.append(''.join(combi))
    countdic=Counter(setMenu)  
    #print(countdic)
    for k,v in countdic.items():
        # print(answer[len(k)])
        if answer[len(k)]==[]:
            answer[len(k)].append((k,v))
            continue
        if answer[len(k)][0][1]==v:
            answer[len(k)].append((k,v))
            continue
        if answer[len(k)][0][1]<v:
            answer[len(k)]=[(k,v)]
            continue
    for ans in answer.values():
        for a,n in ans:
            if n>1:
                answer1.append(a)
    answer1=sorted(answer1)
    return answer1

# 1.메뉴 새로 구성
# 2.각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 3. 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성 (또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함)
# 4. 스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 

# 5. 문자열 또한 알파벳 오름차순으로 정렬

# 1. Counter를 쓸것
# 2. 조합을 쓸것

