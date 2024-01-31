# 25분

import re
from itertools import product

def solution(user_id, banned_id):
    matches = []
    for banned in banned_id:
        pattern = re.compile(banned.replace('*', '.'))
        matches.append([])
        for user in user_id:
            if len(banned) == len(user) and pattern.match(user):
                matches[-1].append(user)
                    
    answer = 0
    history = []
    for p in product(*matches):
        s = set(p)
        if len(p) == len(s) and s not in history:
            history.append(s)
            answer += 1
    
    return answer
