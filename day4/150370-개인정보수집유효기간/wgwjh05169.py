# 7:30~7:56 - 26분

kind_to_term = {}


def solution(today, terms, privacies):
    for term in terms:
        kind, term = term.split(" ")
        term = int(term)
        y, m = term // 12, term % 12
        kind_to_term[kind] = (y, m)
    
    answer = []
    today = [int(token) for token in today.split(".")]
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split(" ")
        if is_over(today, date, kind):
            answer.append(i + 1)
            
    return answer


def is_over(today, date, kind):
    y, m, d = [int(token) for token in date.split(".")]
    y += kind_to_term[kind][0]
    m += kind_to_term[kind][1]
    if m > 12:
        y += 1
        m -=  12
        
    # today[1] += kind_to_term[kind]
    # if today[1] > 12:
    #     today[0] += 1
    #     today[1] -= 12
    # print(date, '->', y, m, d, kind_to_term[kind]) # today가 왜 바뀌지..?
    
    if today[0] < y:
        return False
    if today[0] == y and today[1] < m:
        return False
    if today[0] == y and today[1] == m and today[2] < d:
        return False

    return True
