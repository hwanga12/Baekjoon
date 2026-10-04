def solution(n):
    answer = []

    def move(count, start, end, middle):
        if count == 1:
            answer.append([start, end])
            return

        move(count - 1, start, middle, end)

        answer.append([start, end])

        move(count - 1, middle, end, start)

    move(n, 1, 3, 2)

    return answer