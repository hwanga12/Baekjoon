def solution(numbers):
    ay = [0] * 10
    answer = 0
    for i in range(len(numbers)):
        ay[numbers[i]] += 1
    for j in range(10):
        if ay[j] == 0:
            answer += j
    return answer