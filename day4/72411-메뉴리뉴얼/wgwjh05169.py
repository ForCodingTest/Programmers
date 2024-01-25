# 28분

from itertools import combinations

def solution(orders, course):
    answer = []
    
    count = {}
    for order in orders:
        order = sorted(list(order))
        for c in course:
            cases = combinations(order, c)
            for case in cases:
                case = "".join(case)
                if case in count:
                    count[case] += 1
                else:
                    count[case] = 1
    
    count = [list(t) for t in zip(*sorted(count.items(), key=lambda x: -x[1]))]
    i = count[1].index(1)
    count[0] = count[0][:i]
    count[1] = count[1][:i]
    
    answer = []
    check = {c: 2 for c in course}
    for c in zip(*count):
        string, count = c
        if check[len(string)] > count:
                continue
        
        answer.append(string)
        check[len(string)] = count
    
    return sorted(answer)
