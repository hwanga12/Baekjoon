def solution(my_string, m, c):
    answer = ''
    for i in range(1, len(my_string)//m+1):
        answer+= my_string[(c-1+m*(i-1))]
    return answer
