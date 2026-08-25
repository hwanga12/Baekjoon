def solution(s):
    a = 0  # 변환 횟수
    b = 0  # 제거한 0의 개수

    while s != "1":
        b += s.count("0")

        s = s.replace("0", "")

        s = bin(len(s))[2:]

        a += 1

    return [a, b]