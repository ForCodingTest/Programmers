# 16분

def solution(msg):
    answer = []
    dictionary = [chr(ord('A') + i) for i in range(26)]
    
    i = 0
    c = ''   # msg가 한 글자인 경우, c에 값이 할당되지 않아 UnboundLocalError 발생
    while i < len(msg):
        w = msg[i]
        j = i + 1
        while j < len(msg):
            c = msg[j]
            if w + c not in dictionary:
                break
            w += c
            j += 1
        
        answer.append(dictionary.index(w) + 1)
        dictionary.append(w+c)
        i = j

    return answer
