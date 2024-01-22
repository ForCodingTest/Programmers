# 16분

def solution(msg):
    answer = []
    dictionary = [chr(ord('A') + i) for i in range(26)]
    
    i = 0
    c = ''
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
