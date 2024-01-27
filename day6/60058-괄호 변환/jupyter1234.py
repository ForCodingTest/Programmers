#55분
def solution(p):
    answer = ''
    if not p:
        return p
    if check_right(p):
        return p
    answer = recur(p)
    return answer
    
#입력 -> 개수 동일 균형
#재귀할 함수 (v)
def recur(str):
    conv = {"(":")",")":"("}
    line = "("
    if not str:
        return str
    #2단계
    u,v = split(str)
    print("u",u)
    if check_right(u):
        result = recur(v)
        u += result
        return u
    else:
        result = recur(v)
        print("result",result)
        line += result
        line += ")"
        u = u[1:len(u)-1]
        if u:
            #문자열 immutable!!
            u_list = list(u)
            for idx,c in enumerate(u_list):
                u_list[idx] = conv[c]
            u = ''.join(u_list)
        line += u
        print("line",line)
        return line
    
#올바른 체크
def check_right(str):
    stack = []
    for i in str:
        if i == "(":
            stack.append("(")
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    else:
        return True
def split(str):
    #문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
    open_b = 0
    close_b = 0
    idx = 0
    for idx,s in enumerate(str):
        if s == "(":
            open_b += 1
        else:
            close_b +=1
        if open_b == close_b:
            break
    u = str[:idx+1]
    v = str[idx+1:]
    return u,v
