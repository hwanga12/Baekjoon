def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False

    for i in s:
        if not i.isdigit():
            answer = False
            
    return answer