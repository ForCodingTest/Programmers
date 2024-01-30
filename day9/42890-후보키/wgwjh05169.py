# 30분

from itertools import product
from collections import Counter

def solution(relation):
    unique_keys = []
    for case in list(product([False, True], repeat = len(relation[0]))):
        if is_unique(relation, case):
            case = set([(i if c else None) for i, c in enumerate(case)]) - set([None])
            unique_keys.append(case)
    
    answer = 0
    unique_keys.sort(key = lambda x: len(x))
    for key in unique_keys:
        if is_minimum(unique_keys, key):
            answer += 1
    
    return answer


def is_unique(relation, case):
    # 선택한 속성만 포함하는 릴레이션을 얻음
    temp = list(zip(*relation))
    new_relation = []
    for i, c in enumerate(case):
        if c:
            new_relation.append(temp[i])
        
    if not new_relation:
        return False
    new_relation = list(map(str, zip(*new_relation)))
    
    # 중복된 튜플 검사
    count = Counter(new_relation)
    for c in count.values():
        if c > 1:
            return False
    
    return True
    
    
def is_minimum(unique_keys, key):
    for other in unique_keys:
        if key > other:
            return False
    return True
