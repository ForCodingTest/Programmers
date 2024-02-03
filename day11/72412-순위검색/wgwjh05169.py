from collections import defaultdict
from itertools import product
from itertools import combinations

case = defaultdict(list)

def solution(info, query):

    # 수정1. 집합이 아닌 모든 케이스 적용 -> key를 이용해 탐색하므로 이후 O(1) 가능
    for information in info:
        key, s = information.rsplit(" ", 1)
        s = int(s)
        case[key].append(s)
        
        keys = key.split(" ")
        for i in range(1, 5):
            get_cases(keys, i, s)

    # 수정2. 조건에 부합하는 지원자들의 점수는 외부에서 한 번 정렬, -> 원래 line 30-31 사이에서 정렬했지만 한 번 정렬한 점수를 다시 정렬될 위험 O
    for c in case:
        case[c].sort()
    
    answer = []
    for q in query:
        conditions, k = q.rsplit(" ", 1)
        conditions = conditions.replace(" and ", " ")
        
        if case[conditions] == []:  # 수정1로 인해 조건을 바로 key로 사용할 수 있음
            answer.append(0)
        else:
        # 수정3. python의 .sort()는 NlogN -> 이진탐색 logN으로 수정
            answer.append(binary_search(0, len(case[conditions]) - 1, conditions, int(k)))
            
    return answer


def get_cases(keys, n, s):
    for pos in combinations([0, 1, 2, 3], r=n):
        new_keys = keys[:]
        for p in pos:
            new_keys[p] = '-'
        case[' '.join(new_keys)].append(s)


def binary_search(lo, hi, key, k):
    if case[key][hi] < k:
        return 0
    if lo == hi:
        if case[key][lo] >= k:
            return 1
        return 0
    
    if case[key][lo] < k:
        mid = (lo + hi) // 2
        ans1 = binary_search(lo, mid, key, k)
        ans2 = binary_search(mid + 1, hi, key, k)
        return ans1 + ans2
    else:
        # 수정5. 원래 해당 범위를 모두 k 이상인지 검사했으나, case[key][lo]가 k 이상이라면 해당 범위는 모두 k 이상이므로 단순 연산으로 반환 ===> 가장 오랫동안 놓친 수정...ㅜ
        return hi - lo + 1
        
