def solution(m, n, board):
    answer = 0
    
    #같은거 찾기
    cnt=1
    while True:
        board=[list(i)for i in board]
        target=[]
        for r in range(m-1):   
            for c in range(n-1):
                for addr,addc in ((0,1),(1,0),(1,1)):
                    if board[r][c]!=board[r+addr][c+addc]:
                        break
                else:
                    if board[r][c]!='!':
                        target.append((r,c))  
        if target==[]:
            break
        # #터트리기
        for tarr,tarc in target:
            for addr,addc in ((0,0),(0,1),(1,0),(1,1)):
                board[tarr+addr][tarc+addc]=str(cnt)
        #점수세기
        for r in range(m):
            for c in range(n):
                if board[r][c]==str(cnt):
                    answer+=1
        #중력
        copy=[''.join(i) for i in zip(*board)]
        copy=[i.replace(str(cnt),'')for i in copy]
        copy=['!'*(m-len(i))+i for i in copy]
        #다시바꾸기
        board=[''.join(i) for i in zip(*copy)]
        cnt+=1
    return answer


#5:54
#6:41
# 1.zip으로 행렬 바꾸기
# 2. 2x2 같은지 판단하기
# 3. 블록 내리기
# 2로 돌아가기