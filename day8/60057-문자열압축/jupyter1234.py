#7시43분
def solution(s):
    answer = 0
    # max = len(s)
    #같은 값이 연속해서 나타날 때-> 문자 개수 + 반복되는 값
    case = []    
    for i in range(1,len(s)+1):
        pressed = press(s,i)
        case.append(pressed)
    return min(case)

#가장 짧은 문자열의 길이 반환

#단위길이로 압축
def press(string,cut):
    chunk = []
    while len(string) > cut:
        chunk.append(string[:cut])
        string = string[cut:]
    chunk.append(string)
    chunk.append("")
    new = "" #압축된 문자열
    comp = ""  #비교할 문자열
    count = 1
    #같은 chunk 크기 세기
    for ch in chunk:
        #연속될 때
        if ch == comp:
            count += 1
            
        else:
            #연속아닐 때
            if count > 1:
                #이전에 압축된 게 있으면
                new += str(count)
                new += comp
            else:
                new += comp
            comp = ch
            count = 1
    return len(new)
            
        
            
            
    
    
