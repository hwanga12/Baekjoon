def solution(weights):
    answer = 0
    weights.sort()

    count = {}

    for b in weights:
        answer += count.get(b, 0)

        if (b * 2) % 3 == 0:
            answer += count.get((b * 2) // 3, 0)

        if b % 2 == 0:
            answer += count.get(b // 2, 0)

        if (b * 3) % 4 == 0:
            answer += count.get((b * 3) // 4, 0)

        count[b] = count.get(b, 0) + 1

    return answer