# 8분

def solution(id_list, report, k):
    count = {name: set() for name in id_list}
    for r in report:
        user, target = r.split(" ")
        count[target].add(user)
    
    mail = {name: 0 for name in id_list}
    for target, users in count.items():
        if len(users) >= k:
            for user in users:
                mail[user] += 1
    
    _, answer = zip(*mail.items())
    return answer
