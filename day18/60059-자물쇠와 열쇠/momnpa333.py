import copy

def solution(key, lock):
    answer = True
    L=len(lock)
    # print(iskey(turn(key),lock))
    for r in range(L+1):
        for c in range(L+1):
            for i in range(4):
                key=turn(key)
                for j in range(4):
                    lock=turn(lock)
                    if (iskey((r,c),key,lock)):
                        return True
    return False

def iskey(posi,key,lock):
    R,C=posi
    L=len(key)
    l=len(lock)
    lockcopy=copy.deepcopy(lock)
    for i in range(L):
        for j in range(L):
            if i+R<l and j+C<l:
                lockcopy[i+R][j+C]+=key[i][j]
    for m in range(l):
        for k in range(l):
            if lockcopy[m][k]!=1:
                return False
    return True
                
def turn(key):
    return [list(k[::-1]) for k in zip(*key)]

# 10:33
# 11:34 72퍼
# 11:44 93
# 12:10 완
# 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태
# 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조
# 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.