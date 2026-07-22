def solution(picture, k):
    answer = []

    for row in picture:
        expanded_row = ""

        for pixel in row:
            expanded_row += pixel * k

        for _ in range(k):
            answer.append(expanded_row)

    return answer