#접근과정 풀이봄 누적합 몰랐음...
#대략 1시간 30분
def solution(board, skill):
    #0 ≤ r1 ≤ r2 < board의 행의 길이
    answer = 0
    m = len(board)
    n = len(board[0])
    acsum = [[0] * (n+1) for _ in range(m+1)]
    for s in skill:
        t,r1,c1,r2,c2,d = s
        if t == 1:
            #파괴
            acsum[r1][c1] += -1 * d
            acsum[r1][c2+1] += d
            #열 누적합
            acsum[r2+1][c1] += d
            acsum[r2+1][c2+1] += -1 *d
        else:
            acsum[r1][c1] += d
            acsum[r1][c2+1] += -1 * d
            acsum[r2+1][c1] += -1 * d
            acsum[r2+1][c2+1] += d 
    
    #누적합 계산
    for i in range(m):
        for j in range(n):
            acsum[i][j+1] = acsum[i][j] + acsum[i][j+1]
    for j in range(n):
        for i in range(m):
            acsum[i+1][j] = acsum[i][j] + acsum[i+1][j]
    # print(acsum)
    # print(board)
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] + acsum[i][j] > 0:
                cnt += 1
    return cnt


#0이하가 되어 파괴된 건물도 계속 하락함
#파괴되지 않은 건물의 개수
#type 1 : 공격 2: 회복
#1시44분 끝 아 acsum += 을 안하고 있었음
