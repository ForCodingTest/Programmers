# 18분

def solution(record):
    message = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    
    id_to_name = {}
    answer = []
    for r in record:
        action, uid = r.split(" ", 1)
        if action != 'Leave':
            uid, nickname = uid.split(" ")
        
        if action in message:
            answer.append([uid, message[action]])
            if action == 'Enter':
                id_to_name[uid] = nickname
        else:
            id_to_name[uid] = nickname
    
    i = 0
    while i < len(answer):
        answer[i] = id_to_name[answer[i][0]] + answer[i][1]
        i += 1
        
    return answer
