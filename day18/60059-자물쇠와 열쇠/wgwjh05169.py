n = None
m = None
cnt = 0

def solution(key, lock):
    global n, m, cnt
    n = len(lock)
    m = len(key)
    
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                cnt += 1
    
    if check(key, lock):
        return True
    key = list(map(lambda x: list(reversed(list(x))), zip(*key)))
    if check(key, lock):
        return True
    key = list(map(lambda x: list(reversed(list(x))), zip(*key)))
    if check(key, lock):
        return True
    key = list(map(lambda x: list(reversed(list(x))), zip(*key)))
    if check(key, lock):
        return True

    return False


def check(key, lock):
    for i in range(-1 * m + 1, n):
        for j in range(-1 * m + 1, n):
            if match_key(key, lock, i, j):
                return True
            
    return False


def match_key(key, lock, i, j):
    matched = 0
    for di in range(m):
        for dj in range(m):
            if 0 <= i + di < n and 0 <= j + dj < n:
                if lock[i + di][j + dj] == 0:
                    if key[di][dj] == 0:
                        return False
                    matched += 1
                else:
                    if key[di][dj] == 1:
                        return False
            
    if matched == cnt:
        return True
    return False
