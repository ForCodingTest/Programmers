#2시 25분
def solution(gems):
    part = [] #구간
    cnt = len(set(gems)) #종류 개수
    end = 0
    ishere = {}
    gcnt = 0
    for start,g in enumerate(gems):
        # print(start)
        #end 이동
        while len(ishere) < cnt and end < len(gems):
            if gems[end] not in ishere:
                ishere[gems[end]] = 1
            else:
                ishere[gems[end]] += 1
            gcnt += 1
            end += 1
        if len(ishere) == cnt:
            if part:
                if end -1 - start < part[1] - part[0]:
                    part = [start+1,end]
            else:
                part = [start+1,end]
        # print(ishere,gems[start])
        ishere[g] -= 1
        gcnt -= 1
        if ishere[g] == 0:
            # print(ishere,g)
            del(ishere[g])
    return part

#진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간
#구간은 연속되어야함 (특정범위)
#[시작 번호, 끝 번호]
#start 이동 -> start가 이미 구간에 있을 경우
#end 이동 -> 하나씩 만들어지지 않을 때
