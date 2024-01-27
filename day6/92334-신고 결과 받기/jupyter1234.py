#20분
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    #유저 : 신고 ID
    dict = {}
        #신고당한 횟수
    id_report = {}
    for id in id_list:
        dict[id] = []
        id_report[id] = 0
        
    for r in report:
        to,fr = r.split(" ")
        if fr not in dict[to]:
            dict[to].append(fr)
            id_report[fr] += 1
    for idx,id in enumerate(id_list):
        for to in dict[id]:
            if id_report[to] >= k:
                answer[idx] += 1
    return answer
#동일한 유저 신고 -> 1회로 처리
#k번 이상 신고 -> 정지 -> 신고자 메일
#메일 받은 횟수 반환
