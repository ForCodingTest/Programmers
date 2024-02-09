from collections import deque

def solution(board):
    answer = 0
    answer=findfee(board)
    return answer
def findfee(board):
    dq=deque([])
    ret=[]
    check=[[[float('inf'),float('inf'),float('inf'),float('inf')] for _ in range(len(board))]for _ in range(len(board[0]))]
    # print(check)
    for idx,dirset in enumerate([(0,1),(1,0)]):
        dr,dc=dirset
        # print(idx)
        if 0<=dr<len(board) and 0<=dc<len(board) and board[dr][dc]!=1:
            dq.append((dr,dc,idx,100))
            check[dr][dc][idx]=100
    while dq:
        # print(dq)
        for _ in range(len(dq)):
            r,c,op,fee=dq.popleft()
            # check[r][c][op]=True
            for idx,dirset in enumerate([(0,1),(1,0),(0,-1),(-1,0)]):
                dr,dc=dirset
                curr,curc=r+dr,c+dc
                if 0<=curr<len(board) and 0<=curc<len(board) and board[curr][curc]!=1:
                    if idx!=op:
                        if check[curr][curc][idx]>fee+600:
                            check[curr][curc][idx]=fee+600
                            dq.append((curr,curc,idx,fee+600))
                        if curr==curc and curr==len(board)-1:
                            ret.append(fee+600)
                    else:
                        if check[curr][curc][idx]>fee+100:
                            check[curr][curc][idx]=fee+100
                            dq.append((curr,curc,idx,fee+100))
                        if curr==curc and curr==len(board)-1:
                            ret.append(fee+100)
    # print(ret)
    return min(ret)
# 9:49
# 10:19 52퍼
# 서울와서 마저 풀어서 몇분걸렸는지 체크못함.. 근데 총합 1시간정도 걸린듯 
# board는 2차원 정사각 배열로 배열의 크기는 3 이상 25 이하입니다.
# bfs로 푸는데 가격을 같이 넣어서 하면 될듯