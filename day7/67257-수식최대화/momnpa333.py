from itertools import permutations

def solution(expression):
    answer = []
    op={"+","-","*"}
    exp=[]
    n=""
    for e in expression:
        if e.isdigit():
            n+=e
        else:
            exp.append(int(n))
            exp.append(e)
            n=""
    else:
        exp.append(int(n))
        
    expc=exp[:]
        
    for opset in permutations(op):
        cal=[]
        exp=expc
        for op in opset:
            num=0
            curex=""
            for ex in exp:
                if curex=="+":
                    cal.append(num+ex)
                if curex=="-":
                    cal.append(num-ex)
                if curex=="*":
                    cal.append(num*ex)
                
                if curex:
                    curex=""
                    num=0
                    continue
                    
                if ex ==op:
                    num+=cal.pop()
                    curex=ex
                else:
                    cal.append(ex)
            exp=cal[:]
            cal=[]
        answer.append(abs(exp[0]))
    return max(answer)

# 6:03
# 6:33

# 1.  숫자들과 3가지의 연산문자(+, -, *) 만으로 이루어진 연산 수식
# 2. 새로운 우선순위로 계산 후 가장큰 절대값

# 1. permutaions 사용
# 2. 그에따른 계산