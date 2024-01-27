from collections import Counter

def solution(id_list, report, k):
    answer = []
    repdic={ID:set() for ID in id_list}
    repget=[]
    stop=set()
    for rep in report:
        to,get=rep.split(" ")
        if get not in repdic[to]:
            repget.append(get)
        repdic[to].add(get)
    repget=Counter(repget)
    for name,i in repget.items():
        if i>=k:
            stop.add(name)
    
    for name in repdic.keys():
        answer.append(len(repdic[name]&stop))
    
    return answer
# 00:00
# 00:14
# 1. 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템
# 2. 동일한 유저에 대한 신고 횟수는 1회로
# 3. k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송
# 4. 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송

# 1. 유저별로 신고한 id dic
# 2. 정지된 id 카운트
# 3. 카운트 이상인애들 모아서 알림메일
