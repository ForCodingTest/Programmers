# 45분

directions = [(0, 1), (1, 0), (1, 1)]
    
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    target = [[False for j in range(n)] for i in range(m)]
    
    answer = 0
    count = 0
    while True:
        find_target(board, target, m, n)
        count = remove_and_count(board, target, m, n)
        if count == 0:
            break
        answer += count
        fill_empty(board, m, n)
        
    return answer


def find_target(board, target, m, n):
    global directions
    
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == '0':
                continue
                
            flag = True
            for di, dj in directions:
                if board[i + di][j + dj] != board[i][j]:
                    flag = False
                    break
                    
            if flag:
                target[i][j] = True
                for di, dj in directions:
                    target[i + di][j + dj] = True


def remove_and_count(board, target, m, n):    
    count = 0
    for i in range(m):
        for j in range(n):
            if target[i][j]:
                board[i][j] = '0'
                target[i][j] = False
                count += 1
                
    return count


def fill_empty(board, m, n):
    for _ in range(m-1):
        for i in range(1, m):
            for j in range(n):
                if board[i][j] == '0':
                    board[i][j] = board[i-1][j]
                    board[i-1][j] = '0'
