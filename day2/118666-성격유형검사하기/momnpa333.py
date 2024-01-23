dic={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
def solution(survey, choices):
    answer = ''
    for op,choice in zip(survey,choices):
        op1,op2=op[0],op[1]
        choice-=4
        if choice>0:
            dic[op2]+=choice
        elif choice<0:
            dic[op1]+=abs(choice)
    for op in ("RT","CF","JM","AN"):
        op1,op2=op[0],op[1]
        if dic[op1]>=dic[op2]:
            answer+=op1
        else:
            answer+=op2
            
    
    
    return answer


# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), >프로도형(F)
# 3번 지표	제이지형(J), >무지형(M)
# 4번 지표	어피치형(A), >네오형(N)

# 매우 비동의
# 비동의
# 약간 비동의
# 모르겠음
# 약간 동의
# 동의
# 매우 동의

#7:00
#7:09