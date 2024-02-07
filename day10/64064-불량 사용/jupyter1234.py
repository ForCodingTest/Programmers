from itertools import product
def solution(user_id, banned_id):
    answer = 0
    #각 경우의 수 넣고 조합 구하기
    case = []
    #사용 여부 체크
    for idx_ban,ban in enumerate(banned_id):
        case.append([])
        for idx_user,user in enumerate(user_id):
            if len(user) == len(ban) and comp(user,ban):
                #True면 배열에 추가
                case[-1].append(user)
    # print(case)
    # #조합 구하기
    result = []
    # print(pro)
    for p in product(*case):
        s = set(p)
        if len(s) == len(p) and s not in result:
            result.append(s) # 아 미친 여기서 s를 넣었어야했음!!!!! ㅅㅂ!!!
            answer += 1
    print(result)
    return answer

# * 로 가리기
# user_id 응모자 아이디 목록
# banned_id 불량 사용자 아이디 목록 크기 1이상 user_id 이하
# 제대 아이디 목록의 경우의 수

#비교 유저 아이디와 ban이 주어졌을 때 해당 유저 아이디가 ban이 될 수 있는지
def comp(user,ban):
    for idx,u in enumerate(user):
        if ban[idx] != "*":
            if ban[idx] != u:
            #다름
                return False
    return True
