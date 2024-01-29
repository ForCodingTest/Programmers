from itertools import product

def solution(users, emoticons):
    discount={1:40,2:30,3:20,4:10}
    disSet=[i for i in product((1,2,3,4),repeat=len(emoticons))]
    newemos=[]
    new1=[]
    answer=0
    for dis in disSet:
        count=0
        emoMoneysum=0
        emosum=[]
        for user in users:
            newemo=[]
            userdis,maxmoney=user
            for emo,di in zip(emoticons,dis):
                if userdis<=discount[di]:
                    newemo.append(emo*(1-(discount[di]/100)))
                
            if maxmoney<=sum(newemo):
                count+=1
            else:
                emoMoneysum+=sum(newemo)
                emosum.append(sum(newemo))
        new1.append([count,sum(emosum)])
    new1=sorted(new1,key=lambda x:(-x[0],-x[1]))
    return new1[0]

#7:42
#8:22
# 1. 서비스 가입자 늘리기
# 2. 판매액 늘리기
# 3. 할인율 4개
# 4. 각 사용자들은 자신의 기준에 따라 일정 비율 이상 할인하는 이모티콘을 모두 구매합니다.
# 5. 각 사용자들은 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스에 가입합니다.

# 1. 할인율 permutations
# 2. 할인율 별로 구매비용및 가입여부
