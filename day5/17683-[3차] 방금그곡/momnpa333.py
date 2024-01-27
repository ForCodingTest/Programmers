def solution(m, musicinfos):
    answer = []
    shops={ "C#":"c", "D#":"d", "F#":"f", "G#":"g", "A#":"a"}
    editmusics=[]
    for shop in shops.keys():
        if shop in m:
            m=m.replace(shop,shops[shop])
    for musicinfo in musicinfos:    
        start,finish,name,music=musicinfo.split(",")
        for shop in shops.keys():
            if shop in music:
                music=music.replace(shop,shops[shop])
        startM,startS=map(int,start.split(":"))
        endM,endS=map(int,finish.split(":"))
        time=(endM-startM)*60+endS-startS
        if time<len(music):
            music=music[:time]
        else:
            music=music*1439
            music=music[:time]
        editmusics.append((time,name,music))
        
    for editmusic in editmusics:
        if m in editmusic[2]:
            answer.append(editmusic)
    answer=sorted(answer,key=lambda x:(-x[0]))
    if answer:
        return answer[0][1]
    return  "(None)"

# # 4:20
# # 4:48 런타임에러 전
#4:51
# 1. 노래찾기
# 2. 끝부분 처음부분 연결일수도
# 3. 중간부분이면 해당하는 노래가 여러개일수도 그래서 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교
# 4. 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환
# 5. 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개
# 6. 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복

# 1. 음악을 길이만큼 만들기
# 2. 그 음악에 m이 있는지 확인하기
# 3. 있으면 기간,입력순으로 정렬

# 1. #을 전부다 이름 바꾸기
