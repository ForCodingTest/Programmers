#8시15분
from itertools import product
def solution(users, emoticons):
    #[서비스 가입 수, 이모티콘 매출액] 반환
    answer = []
    #emoticons[i] = 가격
    #각 이모티콘 할인율 모든 경우의 수 다 구해야됨
    sales = list(product([10,20,30,40],repeat = len(emoticons)))
    
    for sale in sales:
        result = cal(users,sale,emoticons)
        answer.append(result)
    answer.sort(key = lambda x :(-x[0],-x[1]))
    return answer[0]
def cal(users,sale,emoticons):
    #계산
    #result = [가입자 수, 이모티콘 총 판매액]
    #users[i] = [기준비율,기준가격]
    result = [0,0]
    for idx,user in enumerate(users):
        cost = 0
        #각 유저별로 계산 이모티콘 계산 -> 비교
        for i,s in enumerate(sale):
            if s >= user[0]:
                cost += (int(emoticons[i] * ((100-s))/100))
        # if sale == (40,40,40,40):
            # print(cost)
        #기준 넘을 경우 서비스 가입
        if cost >= user[1]:
            result[0] += 1
        else:
            result[1] += cost
    # print(sale,result)
    return result
#1번 플러스 서비스가입자 최대한 늘리기
#2번 이모티콘 판매액 최대한 늘리기

#할인율은 10%, 20%, 30%, 40%
#기준 할인율 넘는 임티 다 사기
