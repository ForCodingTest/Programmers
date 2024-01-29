# 33분

from itertools import product

def solution(users, emoticons):
    answer = [-1, -1]
    for d in product(range(10, 41, 10), repeat=len(emoticons)):
        people, payment = get_result(users, emoticons, d)
        if people > answer[0]:
            answer[0] = people
            answer[1] = payment
        elif people == answer[0] and payment > answer[1]:
            answer[0] = people
            answer[1] = payment
            
    return answer


def get_result(users, emoticons, discount):
    people = 0
    total = 0
    for user in users:
        payment = 0
        for emoticon, d in zip(emoticons, discount):
            if d < user[0]:
                continue
            else:
                payment += emoticon - (emoticon * d // 100)
            
            if payment >= user[1]:
                people += 1
                total -= payment
                break
        
        total += payment
        
    return people, total

    
