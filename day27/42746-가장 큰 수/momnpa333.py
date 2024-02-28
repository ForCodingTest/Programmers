def solution(numbers):
    numbers=list(map(str,numbers))
    numbers=sorted(numbers,key=lambda x:x*4)
    if int(''.join(numbers[::-1]))==0:
        return "0"
    return ''.join(numbers[::-1])

#8:00
