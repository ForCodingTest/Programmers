# 14분

def solution(survey, choices):
    score = {"A": 0, "N": 0, "R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0}
    for s, c in zip(survey, choices):
        if 0 < c < 4:
            score[s[0]] += 4 - c
        elif c > 4:
            score[s[1]] += c - 4
    
    types = {"R": "T", "C": "F", "J": "M", "A": "N"}
    ans = ""
    for t1, t2 in types.items():
        ans += t1 if score[t1] >= score[t2] else t2
    
    return ans


# 비동의(1~3): survey[i][0] 에 점수
# 동의일 때(5~7): survey[i][1]  에 점수
