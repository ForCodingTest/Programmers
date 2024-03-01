# 8:23~36 런타임에러 (10점)
# 9:05 (m,n)에 맞춰 puddle 입력 수정

def solution(m, n, puddles):
    puddle = [[False for j in range(m)] for i in range(n)]
    for i, j in puddles:
        puddle[j-1][i-1] = True
        
    memo = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        if puddle[i][0]:
            break
        memo[i][0] = 1
    for j in range(1, m):
        if puddle[0][j]:
            break
        memo[0][j] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if not puddle[i][j]:
                memo[i][j] += memo[i][j-1]
                memo[i][j] += memo[i-1][j]
    
    return memo[-1][-1] % 1000000007

# memo[i][j] = memo[i-1][j] + memo[i][j-1]
