from itertools import combinations
def solution(orders, course):
    #2명 이상 단품메뉴 조합
    #오름차순
    answer = []
    for count in course:
        dict = {}
        for x in orders:
            for case in list(combinations(x,count)):
                #얘 왜 정렬이 안되지 원래 이런가
                case = "".join(sorted(case))
                if case in dict:
                    dict[case] += 1
                else:
                    dict[case] = 1
        print(dict)
        temp = [k for k,v in dict.items() if (v >= 2 and v == max(dict.values()))]  
        answer += temp #append가 아니라 + 임!!!!
    return sorted(answer)
#course : 2부터 10까지 오름차순
#answer : 각 course에 따른 메뉴 조합 오름차순
