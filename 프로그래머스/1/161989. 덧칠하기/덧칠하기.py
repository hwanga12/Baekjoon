def solution(n, m, section):
    answer = 0
    painted_until = 0

    for wall in section:
        if wall > painted_until:
            answer += 1
            painted_until = wall + m - 1

    return answer