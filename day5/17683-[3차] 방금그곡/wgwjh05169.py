# 32분

def solution(m, musicinfos):
    m = replace_melody(m)
    answer = []
    for music in musicinfos:
        start, end, title, info = music.split(",")
        melody = replace_melody(info)
        
        playtime = get_playtime(start, end)
        loop = playtime // len(melody) + 1   # 곡 반복 횟수 - math.ceil() + 1이 더 정확하지만 아랫줄에서 재생시간만큼 슬라이싱해서 간단히 작성
        full_melody = (melody * loop)[:playtime]

        if m in full_melody:
            answer.append((title, playtime))
    
    if answer:
        answer.sort(key = lambda x: -x[1])
        return answer[0][0]
    return "(None)"

def replace_melody(melody):
    melody = melody.replace('A#', 'a')
    melody = melody.replace('C#', 'c')
    melody = melody.replace('D#', 'd')
    melody = melody.replace('F#', 'f')
    melody = melody.replace('G#', 'g')
    return melody


def get_playtime(s, e):
    return get_min(e) - get_min(s)
    
    
def get_min(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m
