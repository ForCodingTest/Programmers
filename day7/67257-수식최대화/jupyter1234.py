from itertools import permutations
#50분
def solution(expression):
    #계산결과 저장
    results = []
    op = []
    sample = ["*","+","-"]
    for i in expression:
        if (i in sample) and (i not in op):
            op.append(i)
    #연산자 조합
    op = list(permutations(op))
    for o_list in op:
        result = abs(cal(expression,o_list))
        results.append(result)
    print("result",results)
    #각각 결과 계산 -> 저장
    #최대값 찾기
    return max(results)
def cal(ex,o_list):
    print(o_list)
    #숫자끼리
    li = []
    temp = ""
    for i in ex:
        if i.isdigit():
            temp += i
        else:
            li.append(int(temp))
            li.append(i)
            temp = ""
    li.append(int(temp))
    for o in o_list:
        idx = 0
        # print(o)
        while len(li) > idx:
            if li[idx] == o:
                # print(idx)
                # 연산자일때
                # 계산하고 결과 넣어주기
                if li[idx] == "*":
                    li[idx-1] = li[idx-1] * li[idx+1]
                    li.pop(idx)
                    li.pop(idx)
                    idx -= 1
                elif li[idx] == "+":
                    li[idx-1] = li[idx-1] + li[idx+1]
                    li.pop(idx)
                    li.pop(idx)
                    idx -= 1
                    print(li)
                else:
                    li[idx-1] = li[idx-1] - li[idx+1]
                    li.pop(idx)
                    li.pop(idx)
                    idx -= 1
            idx += 1
    return li[0]
                
# + - * -> 우선순위 재정의 절댓값이 가장 큰 숫자
