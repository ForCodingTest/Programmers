#57분
def solution(places):
    answer = [] #각 대기실별 거리두기 지킴 여부 1:good 0:bad
    #places : 5 X 5
    
    for i in range(5):
        answer.append(check(places[i]))
    return answer

#p : 앉은 자리
#0 : 빈테이블
#x : 파티션
#맨허튼 거리 (r1, c1), (r2, c2)  2이하 금지 파티션일 땐 허용
# |r1 - r2| + |c1 - c2|
#각 대기실 체크
def check(arr):
    room = []
    dis1 = [[-1,0],[0,-1],[1,0],[0,1]]
    for col in arr:
        temp = []
        for s in col:
            temp.append(s)
        room.append(temp)
    #P주변 체크
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'P':
                for move in dis1:
                    new_i = i+move[0]
                    new_j = j+move[1]
                    if 0<=new_i<=4 and 0<=new_j<=4:
                        if room[new_i][new_j] == 'P':
                            return 0
                        elif room[new_i][new_j] == 'O':
                            for second in dis1:
                                sec_i = new_i + second[0]
                                sec_j = new_j + second[1]
                                if (sec_i != i or sec_j != j) and 0<=sec_i<=4 and 0<=sec_j<=4:
                                    if room[sec_i][sec_j] == 'P':
                                        return 0
    return 1

#case 3,8,31 오류 7시
#if not (sec_i == i and sec_j == j) 이렇게 했어야함 아니면 if (sec_i != i or sec_j != j)
#기존에는 if (sec_i != i or sec_j != j) 이었음
#아 미친 아 아
