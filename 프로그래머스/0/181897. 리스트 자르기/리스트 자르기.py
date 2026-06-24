def solution(n, slicer, num_list):
    answer = []
    a = slicer[0]
    b = slicer[1]
    c = slicer[2]
    
    if n == 1:
        answer = num_list[0:b+1]
    if n == 2:
        answer = num_list[a:]
    if n == 3:
        answer = num_list[a:b+1]
    if n == 4:
        answer = num_list[a:b+1][::c]
    
    return answer