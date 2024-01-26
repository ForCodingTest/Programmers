#40분
#보경아 return 다음에 쓰는 코드는 의미가 없지?
def solution(friends, gifts):
    answer = 0
    board = [[0] * len(friends) for _ in range(len(friends))]
    index = {}
    next_gift = {}
    for idx,name in enumerate(friends):
        index[name] = idx
        next_gift[name] = 0
    #gifts "A B" -> A가 B에게 줌
    for gift in gifts:
        f,r = gift.split(" ")
        board[index[f]][index[r]] += 1
    print(board)
    gift_ex = [0] * len(friends)
    
    # #지수 구하기
    # #받은 선물 -> 열 탐색
    for idx,name in enumerate(friends):
        give = sum(board[index[name]])
        receive = 0
        for i in range(len(friends)):
            receive += board[i][index[name]]
        gift_ex[idx] = give - receive
    # print(gift_ex)
    #다음달 선물 받는 사람 기준으로
    for i in range(len(board)):
        for j in range(len(board)):
            # print("h")
            if board[i][j] > board[j][i]:
                    # i 가 j에게 선물을 더 많이 줌
                    # print(friends[i])
                    next_gift[friends[i]] += 1
            elif board[i][j] == board[j][i]:
                # 지수 비교
                if gift_ex[i] > gift_ex[j]:
                    next_gift[friends[i]] += 1
                
   
    next_gift = sorted(next_gift.items(), key = lambda x:x[1],reverse=True)
    print(next_gift)
    return next_gift[0][1]
#더 많은 선물을 준 사람이 다음 달에 상대에게 선물 받음
#기록이 없거나 같다면 선물 지수가 큰 사람 <- 작은 사람
#선물 지수 = 준 선물의 수 - 받은 선물의 수
#선물 지수까지 같다면 주고받기 x

#선물을 가장 많이 받을 친구가 받을 선물의 수 
