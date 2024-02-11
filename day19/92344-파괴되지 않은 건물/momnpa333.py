from collections import defaultdict
skillset=defaultdict(int)
def solution(board, skill):
    for i in skill:
        op, degree=i[0],i[-1]
        posi=i[1:5]
        # print(",".join(map(str,posi)))
        if op==1:
            skillset[",".join(map(str,posi))]-=degree
        else:
            skillset[",".join(map(str,posi))]+=degree
    for command in skillset:
        game(command,board)
    answer = score(board)
    
    return answer
def game(command,board):
    r1,c1,r2,c2=map(int,command.split(","))
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            board[i][j]+=skillset[command]
            
def score(board):
    score=0
    for rows in board:
        for item in rows:
            if item>0:
                score+=1
    return score
    
    
    
    
# 4:30
# 4:51 정확성, 효율성 2개 통과

# 건물은 적의 공격을 받으면 내구도가 감소하고 내구도가 0이하가 되면 파괴됩니다. 반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 합니다.
# 2개의 건물이 파괴되었다가 복구되고 2개의 건물만 파괴되어있는 상태가 됩니다.
# 내구도가 0 이하가 된 이미 파괴된 건물도, 공격을 받으면 계속해서 내구도가 하락하는 것에 유의해주세요.
# type은 1 혹은 2입니다.
# type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
# type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.
# (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree 만큼 낮추거나 높인다는 뜻입니다.
# 1000*1000*250000-> 말이 되나

# 1. 범위별로 딕셔너리 만들기
# 2. 범위를 합쳐야 할듯 
# 50000*99999=>50억? 효율성 테스트 : 언어별로 작성된 정답 코드의 실행 시간의 적정 배수
def solution(board, skill):
    answer = 0
    sumAry=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for command in skill:
        op, r1, c1, r2, c2, degree=command
        degree= -degree if op==1 else degree
        sumAry[r1][c1]+=degree; sumAry[r2+1][c1]-=degree; sumAry[r1][c2+1]-=degree; sumAry[r2+1][c2+1]+=degree;
    
    for c in range(len(sumAry[0])):
        for r in range(len(sumAry)-1):
            sumAry[r+1][c]+=sumAry[r][c]
    for r in range(len(sumAry)):
        for c in range(len(sumAry[0])-1):
            sumAry[r][c+1]+=sumAry[r][c]
    # print(sumAry)      
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c]+=sumAry[r][c]
            
    return score(board)

def score(board):
    score=0
    for rows in board:
        for item in rows:
            if item>0:
                score+=1
    return score
#5:37 완
#아무리 생각해도 떠오르지 않아서 검색해서 풀었음