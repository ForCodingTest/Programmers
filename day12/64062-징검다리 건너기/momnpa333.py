
def solution(stones, k):
    

    return biSearch(min(stones),max(stones),stones,k)
    # return answer

def isposi(stones,depth,k):
    # stones=[max(0,stone-depth) for stone in stones]
    cnt=0
    for stone in stones:
        if stone-depth<=0:
            cnt+=1
        else:
            cnt=0
        if cnt==k:
            return False
    return True
def biSearch(l,r,stones,k):
    if l>r:
        return l
    mid=(l+r)//2
    if isposi(stones[:],mid,k)==False:
        # print("False")
        return biSearch(l,mid-1,stones[:],k)
    else:
        # print("True")
        return biSearch(mid+1,r,stones[:],k)
    
# # 8:22
# # 8:43 46퍼
# # 8:50 효율성 실패
# 9:47 이진탐색 성공
# # 징검다리는 일렬로 놓여 있고 각 징검다리의 디딤돌에는 모두 숫자가 적혀 있으며 디딤돌의 숫자는 한 번 밟을 때마다 1씩 줄어듭니다.
# # 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며 이때는 그 다음 디딤돌로 한번에 여러 칸을 건너 뛸 수 있습니다.
# # 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.

# # 징검다리를 건너야 하는 니니즈 친구들의 수는 무제한 이라고 간주합니다.
# # stones 배열의 크기는 1 이상 200,000 이하입니다.
# # stones 배열 각 원소들의 값은 1 이상 200,000,000 이하인 자연수입니다.-> 2억??
# # k는 1 이상 stones의 길이 이하인 자연수입니다.

# # 1. k개가 연속으로 0이 나오는지 확인
# # 2. 이진탐색

