from itertools import combinations

from collections import Counter

import heapq
langdic={ lang:idx for idx,lang in enumerate(["-","cpp","java", "python"])}
opdic={op:idx for idx,op in enumerate(["-","backend", "frontend"])}
yeardic={year:idx for idx, year in enumerate(["-","junior", "senior"])}
fooddic={food:idx for idx, food in enumerate(["-","chicken", "pizza"])}
# opnum={idx:dicname for idx,dicname in enumerate(["langdic","opdic","yeardic","fooddic"])}

def solution(info, query):
    answer = []
        
    infoAry=[[[[[]for _ in range(len(fooddic))]for _ in range(len(yeardic))] for _ in range(len(opdic))] for _ in range(len(langdic))]
    for i in info:
        lang,op,year,food,score=i.split()
        lang=langdic[lang]
        op=opdic[op]
        year=yeardic[year]
        food=fooddic[food]
        score=int(score)
        
        infoset=[lang,op,year,food]
        for i in range(5):
            for combis in combinations((0,1,2,3),i):
                infosetc=infoset[:]
                for c in combis:
                    infosetc[c]=0
                infoAry[infosetc[0]][infosetc[1]][infosetc[2]][infosetc[3]].append(score)
            
        
    for i in range(4):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    infoAry[i][j][k][l]=sorted(infoAry[i][j][k][l])
    for q in query:
        q=q.replace("and ","")
        
        lang,op,year,food,score=q.split()
        lang=langdic[lang]
        op=opdic[op]
        year=yeardic[year]
        food=fooddic[food]
        score=int(score)
        opset=[lang,op,year,food]
        answer.append(findnum(infoAry,opset,score))
    
    return answer
def findnum(infoAry,opset,score):
    num=0
    num+=calnum3(infoAry[opset[0]][opset[1]][opset[2]][opset[3]],score)
    return num

def calnum3(calAry,score):
    return len(calAry)-biSearch(calAry,0,len(calAry)-1,score-0.1)
def biSearch(ary,l,r,tar):
    if l>r:
        return l
    m=(l+r)//2
    if ary[m]==tar:
        return m
    if ary[m]<tar:
        return biSearch(ary,m+1,r,tar)
    if ary[m]>tar:
        return biSearch(ary,l,m-1,tar)



# 10:32
# 11:59 효율성 제외 통과
# 12:35 효율성 2개 안됨
# 1:01 통과
# 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다
# * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

# 개발언어는 cpp, java, python 중 하나입니다.
# 직군은 backend, frontend 중 하나입니다.
# 경력은 junior, senior 중 하나입니다.
# 소울푸드는 chicken, pizza 중 하나입니다.

# 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
# query 배열의 크기는 1 이상 100,000 이하입니다

# 언어는 cpp, java, python, - 중 하나입니다.
# 직군은 backend, frontend, - 중 하나입니다.
# 경력은 junior, senior, - 중 하나입니다.
# 소울푸드는 chicken, pizza, - 중 하나입니다.
# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
# X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.

# 1.info, query 파싱후 딕셔너리 배열만들기 [언어,직군,경력,음식,점수]
# 2. 10만 10만이기 때문에 정렬을 힙으로 하기 점수를 기준으로 10만 * 10만 은 100억?
# 3. info 카피를 하나씩 빼면서 그에 맞는 점수나올때 까지 pop