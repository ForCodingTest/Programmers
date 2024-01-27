from collections import Counter

def solution(friends, gifts):
    answer = 0
    result=[]
    dic={}
    giftarr=[[0]*len(friends)for _ in range(len(friends))]
    giftscore=[0]*len(friends)
    for idx,friend in enumerate(friends):
        dic[friend]=idx
    for gift in gifts:
        give,take=gift.split(" ")
        giftarr[dic[give]][dic[take]]+=1
    for idx,arr in enumerate(giftarr):
        giftscore[idx]+=sum(arr)
    for idx,arr in enumerate(zip(*giftarr)):
        giftscore[idx]-=sum(arr)
    
    for i in range(len(giftarr)):
        for j in range(len(giftarr)):
            if i<=j:
                continue
            if giftarr[i][j]>giftarr[j][i]:
                result.append(i)
            elif giftarr[i][j]<giftarr[j][i]:
                result.append(j)
            else:
                if giftscore[i]>giftscore[j]:
                    result.append(i)
                elif giftscore[i]<giftscore[j]:
                    result.append(j)
    result=list(Counter(result).values())
    if result:
        return max(result)
    
    return answer
# 3:48
# 4:19
# 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
# 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
# 선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
# 만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.

# 1.사람별로 주고 받은 표 그리기
# 2. 선물지수 구하기
# 3. 두사람 사이에 더 많은 선물을 준 사람 구하기
# 4. 같다면 선물지수 낮은사람이 선물해주기
