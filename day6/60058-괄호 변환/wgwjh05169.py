# 20분

def solution(p):
    return get_correct(p)


def get_correct(w):
    if w == '':
        return ''
    
    count = 0
    u, v = '', ''
    for i in range(len(w)):
        if w[i] == '(': count += 1
        else: count -= 1
        
        if count == 0:
            u = w[:i+1]
            if i < len(w) - 1:
                v = w[i+1:]
            break
    
    reverse = {'(': ')', ')': '('}
    if is_correct(u):
        return u + get_correct(v)
    else:
        u = u[1:-1]
        return '(' + get_correct(v) + ')' + ''.join(list(map(lambda x: reverse[x], list(u))))


def is_correct(u):
    stack = []
    for c in u:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True
