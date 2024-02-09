from collections import deque
#try1 테케 11,13,16,17,18,19,25 실패...시발시발시발
#try2 가로 세로가 아니라 동서남북 다 돌면서 각각의 경우의 수 모두 돌기
#try3 큐에 가격을 저장 안 했었음! cost_board 값이 아니라 큐에 있는 가격으로 연산했어야함
def solution(board):
    # build(board,[0,0,True])
    # build(board,[0,0,False])
    return min(build(board,[0,0,0,0]),build(board,[0,0,3,0]))
def build(board,start):
    n = len(board)
    # visited = [[False] * n for _ in range(n)]
    cost_board = [[float('inf')] * n for _ in range(n)]
    cost_board[0][0] = 0
    #상하 
    ud = ([1,0],[-1,0])
    lr = ([0,-1],[0,1])
    d = ([1,0],[-1,0],[0,-1],[0,1]) #우 좌 상 하
    #bfs
    w = deque([start])
    while w:
        # print(w)
        # print(cost_board)
        r,c,f,cost = w.popleft()
        for i in range(4):
            nr = r + d[i][0]
            nc = c + d[i][1]
            if (0<=nr<n and 0<=nc<n) and board[nr][nc] == 0:
                new = cost + 100
                if i != f: 
                    new = new + 500
                if cost_board[nr][nc] >= new:
                    cost_board[nr][nc] = new
                    w.append((nr,nc,i,new))
    return cost_board[n-1][n-1]
       
        
# 0 : 빔 1: 벽(건설x)
# (0,0) ~ (N-1,N-1)
#직선 : 100원 코너 : 500원 
#경주로 : 두 빈칸 연결 -> 직선 하나
#경주로 최소 비용 (코너 최소화)
#다 구하고 최소값?
