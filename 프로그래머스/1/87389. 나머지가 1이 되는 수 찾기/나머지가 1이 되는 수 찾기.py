def solution(n):
    answer = 0
    ay = []
    for i in range(1, n):
        if n % i == 1:
            ay.append(i)
    return ay[0]