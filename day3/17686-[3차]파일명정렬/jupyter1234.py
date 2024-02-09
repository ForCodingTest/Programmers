#11시 25분 시작
#11시43분 런타임에러 why? why!
#1. head가 한글자인경우
#2. tail이 없는경우
#해결 12시3분
def solution(files):
    #head, number, tail
    dict = {k:v for k,v in enumerate(files)}
    print(dict)
    arr = []
    for index,f in enumerate(files):
        temp = []
        rest = ""
        for idx,i in enumerate(f):
            #head랑 숫자 쪼개기
            if i.isdigit():
                #문자가 한글자인 경우
                if idx == 1:
                    rest = f[idx:]
                    print(rest)
                    temp.append(f[0].lower())
                else:
                    rest = f[idx:]
                    temp.append(f[:idx].lower())
                break
        flag = False
        for idx,r in enumerate(rest):
            #number 빼내기
            if not r.isdigit():
                # print(r)
                num = rest[:idx]
                print(num)
                if len(num) >= 5:
                    print(num[:5])
                    temp.append(int(num[:5]))
                else:
                    temp.append(int(num))
                flag = True
                temp.append(index)
                arr.append(temp)
                break
        #tail이 없는경우
        if not flag:
            if len(rest) > 5:
                temp.append(int(rest[:5]))
            else:
                temp.append(int(rest))
            temp.append(index)
            arr.append(temp)
    sorted_list = []
    
    arr = sorted(arr,key=lambda x: [x[0],x[1],x[2]])
    for a in arr:
        idx = a[2]
        sorted_list.append(dict[idx])
    print(sorted_list)
    return sorted_list
                
"""
정렬기준
1. head -> 사전 순 대소문자 구분 X
2. 숫자 순 
3. 입력 순
"""
