udic={}
def solution(record):
    answer = []
    for rec in record:
        rec=rec.split(" ")
        if rec[0]=="Enter":
            udic[rec[1]]=rec[2]
        if rec[0]=="Change":
            udic[rec[1]]=rec[2]
    for rec in record:
        rec=rec.split(" ")
        if rec[0]=="Enter":
            answer.append(udic[rec[1]]+"님이 들어왔습니다.")
        if rec[0]=="Leave":
            answer.append(udic[rec[1]]+"님이 나갔습니다.")
            
        
    
    return answer

# 아닌 가상의 닉네임을 사용하여 채팅방에 들어갈 수 있다.
# 해, 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창

# 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
# 채팅방에서 닉네임을 변경한다.

# 1. id 별 닉네임 사전
# 2. 사전으로 result 구현
#7:10
#7:17