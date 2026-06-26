def solution(myString, pat):
    answer = ''
    
    for i in range(len(myString) - 1, -1, -1):
        if myString[i:i + len(pat)] == pat:
            answer = myString[:i + len(pat)]
            break
    
    return answer