def solution(s):
    answer = []
    groups = s[2:-2].split("},{")
    groups = [list(map(int, group.split(","))) for group in groups]

    groups.sort(key=len)
    seen = set()

    for group in groups:
        for number in group:
            if number not in seen:
                answer.append(number)
                seen.add(number)
                break
    return answer