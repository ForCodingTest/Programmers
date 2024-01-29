def solution(s):
    answer = set()
    
    for t in range(1,len(s)):
        strT=""
        op=""
        cnt=1
        for i in range(1,len(s)+1):
            if s[(i-1)*t:i*t]==op:
                cnt+=1
            else:
                if cnt>1:
                    strT+=str(cnt)+op
                elif cnt==1:
                    strT+=op
                op=s[(i-1)*t:i*t]
                cnt=1
            if s[(i-1)*t:i*t]=="":
                break
        else:
            strT+=str(cnt)+op
            op=s[(i-1)*t:i*t]
            cnt=1
        answer.add(len(strT))
    if answer:
        return min(answer)
    return 1
#7:20
#7:39 런타임 error
#7:41
# 1. 문자열 압축

# 1.길이 별로 압축하기
# 2.가장 짧은것 return
# 3. 