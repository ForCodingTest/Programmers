dic={}

def solution(msg):
    answer = []
    for num, alpa in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        dic[alpa]=num+1
    num=27
    w=""
    while len(msg)>1:
        for idx,nxt in enumerate(msg):
            if w+nxt in dic:
                w+=nxt
                continue
            if w+nxt not in dic:
                answer.append(dic[w])
                dic[w+nxt]=num
                num+=1
                w=""
                msg=msg[idx:]
                break
        else:
            answer.append(dic[msg])
            return answer
    answer.append(dic[msg])   
        # if w in dic:
        #     answer.append(w)
        # if c and (w+c) not in dic:
        #     dic[w+c]:num
        #     num+=1
            
    return answer

# 10시 44분
# 11시 20분

# 1. 단어 압축하기

# 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화
# 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾음
# 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거
# 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 5. 단계 2로 돌아간다.