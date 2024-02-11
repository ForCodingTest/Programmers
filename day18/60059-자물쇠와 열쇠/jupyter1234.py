#11시2분 시작
#11시51분 2,4,12(re) 1,23-33 실패 (크기가 다른 배열을 zip으로 묶음)
#돌기 & 돌기 체크 안 함
#왜 고칠 수록 점수가 낮아질까

#2,4,12 lock이 모두 1인 경우 -> 그냥 열림 
def solution(key, lock):
    answer = True 
    lockSlot = [] #채워야할 자물쇠의 홈
    #자물쇠 홈 찾기
    ll = len(lock)
    tl = len(key)
    dcnt = 0
    for i in range(ll):
        for j in range(ll):
            if lock[i][j] == 0:
                lockSlot.append([i,j])
            else:
                dcnt += 1
    if dcnt == ll * ll > 0:
        return True
    #회전은 4번
    #자물쇠의 모든 홈이 메꿔지는지 확인 단 자물쇠의 1과 열쇠의 1이 만나면 안됨
    #90도 회전 -> y=x 대칭 (바꿔여됨)
    for _ in range(4):
        #돌리고 check
        breaker = False
        turn,key = turn_key(key) #회전
        # print(turn) 잘 돌아감 이게 문제는 아님
        for i in range(1,ll+tl):
            for j in range(1,ll+tl):
                moved = [[t[0]-tl+i,t[1]-tl+j] for t in turn if 0<=t[0]-tl+i<ll and 0<=t[1]-tl+j<ll]
                if check(moved,lock,ll):
                    return True
    return False
def turn_key(key):
    turn = [] #열쇠의 돌기 좌표 
    new = [[0] * len(key) for _ in range(len(key))]
    p = len(key) - 1
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                new[j][p-i] = 1
                turn.append([j,p-i])
    return turn,new
def check(moved,lock,ll):
    forcheck = [[0] * ll for _ in range(ll)]
    for m in moved:
        forcheck[m[0]][m[1]] = 1
    for i in range(ll):
        for j in range(ll):
            if lock[i][j] + forcheck[i][j] != 1:
                return False
    return True
#자물쇠 NxN 열쇠 MxM ("회전"과 "이동" 가능)
#홈(자물쇠) & 돌기(열쇠) 돌기와 돌기는 만나면 안됨
#자물쇠의 모든 홈을 채워야함 가능-> True 불가능 -> False
#0:홈 1:돌기
