def solution(today, terms, privacies):
    answer = []
    dates=[]
    dic={}
    for term in terms:
        op,length=term.split(" ")
        dic[op]=length
    
    for privacy in privacies:
        date,op=privacy.split(" ")
        date=list(map(int,date.split(".")))
        date[1]+=int(dic[op])
        while date[1]>12:
            date[0]+=1
            date[1]-=12
        dates.append(date)
    
    for idx,date in enumerate(dates):
        if vali(today,date)==False:
            answer.append(idx+1)
    
    return answer
def vali(today,date):
    today=list(map(int,today.split(".")))
    todaySum=today[0]*12*28+today[1]*28+today[2]
    dateSum=date[0]*12*28+date[1]*28+date[2]
    if todaySum<dateSum:
        return True
    else:
        return False
# 1. 유효기간
# 2. 종류별 기간

# 1. 같은날짜면 파기하기
