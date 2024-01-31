from itertools import combinations, permutations

def solution(user_id, banned_id):
    answer = []
    
    for combi in combinations(user_id,len(banned_id)):
        for permu in permutations(combi):
            if check(permu,banned_id):
                if set(permu) not in answer:
                    answer.append(set(permu))
    
    return len(answer)
def check(permu,banned_id):
    for p,b in zip(permu,banned_id):
        if len(p)==len(b):
            for ps,bs in zip(p,b):
                if bs != '*' and ps!=bs:
                    return False
        else:
            return False
    else:
        return True
    return False
# 1.  이 때 개인정보 보호을 위해 사용자 아이디 중 일부 문자를 '*' 문자로 가려서 전달했습니다. 가리고자 하는 문자 하나에 '*' 문자 하나를 사용하였고 아이디 당 최소 하나 이상의 '*' 문자를 사용

# 2. user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
# 응모한 사용자 아이디들은 서로 중복되지 않습니다.
# 응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.
# 3.  banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
# 불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다.
# 불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
# 불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.

# 1. 글자수 별로 모든 * 경우의 수 만들기 2의 1승 ~2의 8승 더하기
# 2. 그걸 permutation 해서 되는지 확인하고 되면 바로 break
# 만들어서 겹치는지 확인
#9:29
