#28분 하드코딩 때림............
def solution(survey, choices):
    # 1 2 3 : 첫번째 지표
    # 5 6 7: 두번째 지표
    arr = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    pm = [2,0,-2]
    answer = ""
    for s in range(len(survey)):
        #"AN"
        if 1<= choices[s] <= 3:
            arr[survey[s][0]] += (choices[s]+pm[choices[s]-1])
        elif choices[s] == 4:
            continue
        else:
            arr[survey[s][1]] += choices[s] - 4
    #계산
    if arr['T'] > arr['R']: answer += 'T' 
    else: answer += 'R'
    if arr['F'] > arr['C']: answer+= 'F' 
    else: answer += 'C'
    if arr['M'] > arr['J']: answer += 'M' 
    else : answer += 'J'
    if arr['N'] > arr['A']: answer += 'N' 
    else : answer += 'A'
        
    return answer
"""
1. R T
2. C F
3. J M
4. A N
크기는 고정정 3 2 1 0 1 2 3
점수가 같은 경우 사전 순으로 빠른 성격 유형
choices[i] 는 i+1번째 질문의 선택지   1부터 7까지 있음 주의
survey[i][0] : 비동의 관련 선택지
survey[i][1] : 동의 관련 선택지
"""
