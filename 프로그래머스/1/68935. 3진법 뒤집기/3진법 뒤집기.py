def solution(n):
    answer = 0
    ay = ''

    while n > 0:
        ay += str(n % 3)
        n //= 3

    for i in range(len(ay)):
        answer += int(ay[i]) * (3 ** (len(ay) - 1 - i))

    return answer