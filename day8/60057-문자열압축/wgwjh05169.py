# 37분

def solution(s):
    answer = 0
    
    memory = []
    memory.append(split_byn(s, 1))
    if len(s) < 2:
        return calculate(memory[0])
    
    for i in range(2, len(s)):
        if i % 2 == 1:
            memory.append(split_byn(s, i))
        else:
            memory.append(scailing(memory[i // 2 - 1]))
    
    return min(calculate(tokens) for tokens in memory)


def split_byn(string, n):
    tokens = []
    while string:
        tokens.append(string[:n])
        string = string[n:]
    
    return tokens

def scailing(array):
    copy = array[:]
    new_arr = []
    while copy:
        if len(copy) > 1:
            new_arr.append(copy.pop(0)+copy.pop(0))
        else:
            new_arr.append(copy.pop(0))
    
    return new_arr


def calculate(tokens):
    result = []
    while tokens:
        token = tokens.pop(0)
        if result and token == result[-1]:
            if len(result) > 1 and result[-2].isdigit():
                result[-2] = str(int(result[-2]) + 1)
            else:
                result.insert(-1, '2')
        else:
            result.append(token)
    
    return len(''.join(result))
