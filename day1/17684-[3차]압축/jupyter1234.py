#22분
def solution(msg):
    answer = []
    dict = {}
    init = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        dict[init[i]] = i+1
    find_len = 1
    index = -1
    dict_size = 27
    i = len(msg)
    while i >= 1:
        while find_len <= len(msg):
            if msg[:find_len] in dict:
                # print(msg[:find_len])
                index = dict[msg[:find_len]]
                find_len += 1
                # print(index)
            else:
                find_len -= 1
                break
        answer.append(index)
        dict[msg[:find_len+1]] = dict_size
        dict_size += 1
        msg = msg[find_len:]
        i = len(msg)
        find_len = 1
    return answer

#사전에 있는 가장 긴 문자열 W 
# w의 색인 번호 출력 후 w 제거
# w+c(한글자) -> 사전
