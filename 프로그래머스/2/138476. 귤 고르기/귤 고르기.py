def solution(k, tangerine):
    dic_ = {}

    for x in tangerine:
        if x in dic_:
            dic_[x] += 1
        else:
            dic_[x] = 1

    counts = sorted(dic_.values(), reverse=True)

    answer = 0

    for count in counts:
        k -= count
        answer += 1

        if k <= 0:
            break

    return answer