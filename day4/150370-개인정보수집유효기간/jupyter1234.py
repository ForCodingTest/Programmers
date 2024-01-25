def solution(today, terms, privacies):
    answer = []
    
    # terms "약관 종류 유효기간"
    #privacies[i]는 i+1번 개인정보의 수집 일자와 약관 종류 "YYYY.MM.DD 약관 종류"
    #날짜는 today 이전 날짜
    #1월 5일 -> 12개월 -> 내년 1월 5일 파기
    days = 28 #두자리 01, 28
    
    today = today.split(".")
    for i in range(3):
        today[i] = int(today[i])
    #계약
    dead = []
    #privacies 쪼개기
    for i in range(len(privacies)):
        dead.append(privacies[i].split(" "))
        dead[i][0] = dead[i][0].split(".")
        dead[i][0][0] = int(dead[i][0][0])
        dead[i][0][1] = int(dead[i][0][1])
        dead[i][0][2] = int(dead[i][0][2])
    # print(dead)
    # [['2021', '05', '02'], 'A']
    #약관 쪼개기
    term = {}
    for i in range(len(terms)):
        temp = terms[i].split(" ")
        term[temp[0]] = int(temp[1])
    #파기 날짜 구하기
    #7
    for i in dead:
        dur = term[i[1]]
        i[0][0] += (dur // 12)
        i[0][1] += (dur % 12)
        if i[0][1] > 12:
            i[0][0] += 1
            i[0][1] -= 12
    print(dead)
    
    #오늘날짜랑 비교
    #today "YYYY.MM.DD"
    idx = 1
    for d in dead:
        #년도비교
        if d[0][0] < today[0]:
            answer.append(idx)
        elif d[0][0] == today[0]:
            #달비교
            if d[0][1] < today[1]:
                answer.append(idx)
            elif d[0][1] == today[1]:
                #날짜비교
                if d[0][2] <= today[2]:
                    answer.append(idx)
        idx += 1
    
        
            
    return answer
