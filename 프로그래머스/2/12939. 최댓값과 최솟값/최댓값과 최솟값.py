def solution(s):
    ay = s.split()
    by = []

    for i in range(len(ay)):
        by.append(int(ay[i]))

    answer = str(min(by))
    answer += ' '
    answer += str(max(by))

    return answer