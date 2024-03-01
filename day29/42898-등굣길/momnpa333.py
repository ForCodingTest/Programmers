from collections import deque

def solution(m, n, puddles):
    answer = 0
    route=[[0]*m for _ in range(n)]
    check=[[False]*m for _ in range(n)]
    # puddles.append([3,2])
    for pud in puddles:
        c,r=pud
        route[r-1][c-1]="!"
    bfs(route,check)
    return route[n-1][m-1]%1000000007

def bfs(route,check):
    dq=deque([])
    dq.append([0,0])
    route[0][0]=1
    check[0][0]=True
    
    while dq:
        for _ in range(len(dq)):
            x,y=dq.popleft()
            for addx,addy in ((-1,0),(0,-1)):
                if 0<=x+addx<len(route) and 0<=y+addy<len(route[0]) and route[x+addx][y+addy]!="!":
                    route[x][y]+=route[x+addx][y+addy]
            for addx,addy in ((0,1),(1,0)):
                if 0<=x+addx<len(route) and 0<=y+addy<len(route[0])and route[x+addx][y+addy]!="!" and check[x+addx][y+addy]==False:
                    dq.append([x+addx,y+addy])
                    check[x+addx][y+addy]=True
                
#8:18
    
    
    
    
    