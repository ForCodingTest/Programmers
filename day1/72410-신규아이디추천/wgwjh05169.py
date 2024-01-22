# 시간 재는 거 깜빡함! 쏘리

def solution(new_id):
    answer = ''
    usable = ('-', '_')
    for char in new_id.lower():
        if char.isalnum():
            answer += char
        elif char in usable:
            answer += char
        elif char == '.' and len(answer) > 0 and answer[-1] != '.':
            answer += char

    answer = answer.lstrip('.').rstrip('.')
    
    if answer == '':
        answer = 'a'
        
    if len(answer) > 15:
        answer = answer[:15].rstrip('.')
    elif len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))
    
    return answer
