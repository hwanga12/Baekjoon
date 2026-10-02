def solution(p):
    # 빈 문자열이면 종료
    if p == '':
        return ''

    balance = 0
    correct = True

    # 가장 작은 균형잡힌 문자열 u의 끝 위치 찾기
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1

        # 중간에 음수가 되면 u는 올바르지 않음
        if balance < 0:
            correct = False

        # 처음으로 균형이 맞는 순간
        if balance == 0:
            break

    u = p[:i + 1]
    v = p[i + 1:]

    # u가 올바르면 그대로 두고 v만 재귀 처리
    if correct:
        return u + solution(v)

    # u가 올바르지 않으면 문제의 변환 규칙 적용
    result = '('
    result += solution(v)
    result += ')'

    for char in u[1:-1]:
        if char == '(':
            result += ')'
        else:
            result += '('

    return result