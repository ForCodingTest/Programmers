size = 0
def solution(n, k, cmd):
    global size
    size = n
    # answer = ""
    answer = ["O"] * n
    #n : 행개수 k:처음위치
    dict = {}
    deleted = []
    dict[0] = [None,1]
    for i in range(1,n-1):
        dict[i] = [i-1,i+1]
    dict[n-1] = [n-2,None]
    # print(dict)
    #["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
    for c in cmd:
        if c.startswith('D'):
            _,m = c.split(" ")
            #m이 두자리수이상일 경우를 생각못했음!!!!!!
            k = down(dict,k,int(m))
        elif c.startswith('U'):
            _,m = c.split(" ")
            k = up(dict,k,int(m))
        elif c =='C':
            deleted.append(k)
            k = delete(dict,k)
        elif c == 'Z':
            idx = deleted.pop()
            recover(dict,idx)
    #삭제된 인덱스 확인
    # for d in dict:
    #     if dict[d][2] == True:
    #         answer += "O"
    #     else:
    #         answer += "X"
    if deleted:
        for d in deleted:
            answer[d] = "X"
    return "".join(answer)
def down(dict,k,m):
    for _ in range(m):
        k = dict[k][1]
    return k

def up(dict,k,m):
    for _ in range(m):
        k = dict[k][0]
    return k
def delete(dict,k):
    prev = dict[k][0]
    nxt = dict[k][1]
    if prev != None:
        dict[prev][1] = nxt
    if nxt != None:
        dict[nxt][0] = prev
        k = nxt
    else:
        k = prev
    return k
def recover(dict,idx):
    #복구
    if dict[idx][0] != None:
        prev = dict[idx][0]
        dict[prev][1] = idx
    if dict[idx][1] != None:
        nxt= dict[idx][1]
        dict[nxt][0] = idx
    
#연결리스트?
#U X 위 D X 아래 C 현재 선택된 행 삭제, 바로 아래 행 선택, Z삭제 복구 원래대로 복구
#명령 후 표와 처음 표 비교 삭제 -> O 삭제x->x 문자열
