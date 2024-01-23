#30분
def solution(new_id):
    answer = ''
    #-_.~!@#$%^&*()=+[{]}:?,<>/
    del_str = "~!@#$%^&*()=+[{]}:?,<>/"
    #규칙 맞지 않을 때 -> 유사하면서 규칙에 맞는 아이디
    # 3<=len<=15
    #알파벳 소문자 , 숫자, - , _ , .
    #.는 처음과 끝 x 연속 x
    #step1
    new_id = new_id.lower()
    new_id = list(new_id)
    #step2
    i = 0
    new_id_2 = []
    for i in new_id:
        if i not in del_str:
            new_id_2.append(i)
    #step3 . 2개 이상
    i = 0
    while i < len(new_id_2) -1 :
        if new_id_2[i] == "." and new_id_2[i+1] == ".":
            new_id_2.pop(i+1)
        else :
            i += 1
    #step4
    if new_id_2 and new_id_2[0] == ".":
        new_id_2.pop(0)
    if new_id_2 and new_id_2[-1] == ".":
        new_id_2.pop()
    #step5
    if not new_id_2:
        new_id_2.append("a")
    #step6
    if len(new_id_2) >= 16:
        new_id_2 = new_id_2[:15]
        if new_id_2[-1] == ".":
            new_id_2.pop()
    #step7
    if len(new_id_2) <= 2:
        last = new_id_2[-1]
        while len(new_id_2) < 3:
            new_id_2.append(last)
    for i in new_id_2:
        answer += i
    return answer
