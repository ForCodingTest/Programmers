# 28분

def solution(files):
    array = []
    idx_to_file = {}
    i = 0
    while i < len(files):
        idx_to_file[i] = files[i]
        head, num = split_filename(files[i])
        array.append([i, head, num])
        i += 1
    
    answer = []
    array.sort(key=lambda x: [x[1], int(x[2])])
    for i, h, n in array:
        answer.append(idx_to_file[i])
    
    return answer


def split_filename(filename):
    h, n = '', ''
    i = 0
    while i < len(filename):
        if filename[i].isdigit():
            for _ in range(5):
                n += filename[i]
                i += 1
                if i >= len(filename) or not filename[i].isdigit():
                    return h.lower(), n
            
        h += filename[i]
        i += 1
        
    return h.lower(), n
