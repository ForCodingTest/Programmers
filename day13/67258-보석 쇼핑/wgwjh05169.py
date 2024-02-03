from collections import defaultdict

def solution(gems):
    condition = len(set(gems))  # 구간이 포함해야 하는 최소한의 보석 개수
    count = defaultdict(int)    # 구간에 포함된 보석 종류별 개수
    
    for i in range(0, condition):  # 최초 구간 = gems[0:condition]
        count[gems[i]] += 1
    if len(count) == condition:
        return [1, condition]
    
    lo = -1
    hi = condition - 1
    ans = [1, 100000]
    while lo < len(gems) - 1 and hi < len(gems) - 1:
        # 모든 종류의 보석을 모을 때까지 구간 끝을 오른쪽으로 확장
        while len(count) != condition and hi < len(gems) - 1:
            hi += 1
            count[gems[hi]] += 1

        # 한 종류의 보석이 제거될 때까지 구간 시작을 오른쪽으로 축소
        while len(count) == condition and lo <= hi:
            lo += 1
            if count[gems[lo]] > 1:
                count[gems[lo]] -= 1
            else:
                count.pop(gems[lo])

      # 해당 구간이 현재까지 중 가장 좁은 구간이면 ans에 저장
        if hi - lo < ans[1] - ans[0]:
            ans = [lo + 1, hi + 1]
                
    return ans


# 이중 포인터를 활용한 O(N) 풀이
# 처음에 슬라이딩 윈도우를 활용했지만 O(NK)로 실패 (K = 윈도우의 크기)
