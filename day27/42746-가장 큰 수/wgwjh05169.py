import heapq

def solution(numbers):
    n = len(numbers)
    
    heap = []
    for num in numbers:
        n = list(map(lambda x: -int(x), str(num)))
        heap.append(n)
    heapq.heapify(heap)
    
    digit = {}
    while heap:
        num = heapq.heappop(heap)
        first = -num[0]
        if not digit.get(first):
            digit[first] = []
        num = ''.join(map(str, list(map(lambda x: -x, num))))
        digit[first].append(num)
    
    ans = ''
    for k, vs in digit.items():
        for i in range(len(vs) - 1):
            if not is_correct(vs[i], vs[i+1]):
                vs[i], vs[i+1] = vs[i+1], vs[i]
        
        ans += ''.join(vs)
    
    return ans
            
            
def is_correct(v1, v2):
    if len(v1) == len(v2):
        return True

    li = len(v1)
    if v2[li - 1] < v2[li]:
        return False
    
    return True
        
    
# 8:05~8:27 1번 테케 통과
# 9:07~9:32 런타임 에러 46.7
