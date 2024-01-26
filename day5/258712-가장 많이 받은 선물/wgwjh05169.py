# 23분

def solution(friends, gifts):
    # record[A][B]: A가 B에게 선물한 횟수
    idx = {name: i for i, name in enumerate(friends)}
    record = [[0 for j in range(len(friends))] for i in range(len(friends))]
    for gift in gifts:
        A, B = gift.split(" ")
        A, B = idx[A], idx[B]
        record[A][B] += 1
    
    # 선물지수
    score = {idx[name]: 0 for name in friends}
    for A in range(len(friends)):
        score[A] += sum(record[A])
        score[A] -= sum(list(zip(*record))[A])
    
    # 받을 선물 계산
    recieve = {idx[name]: 0 for name in friends}
    for A in range(len(friends)):
        for B in range(len(friends)):
            if record[A][B] > record[B][A]:
                recieve[A] += 1
            elif record[A][B] < record[B][A]:
                recieve[B] += 1
            elif score[A] > score[B]:
                recieve[A] += 1
            elif score[A] < score[B]:
                recieve[B] += 1
    
    answer = sorted(recieve.items(), key=lambda x: -x[1])[0][1] // 2
    return answer
