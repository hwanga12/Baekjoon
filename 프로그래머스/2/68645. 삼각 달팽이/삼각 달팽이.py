def solution(n):
    triangle = [
        [0] * (row + 1)
        for row in range(n)
    ]

    directions = [
        (1, 0),
        (0, 1),
        (-1, -1)
    ]

    row = 0
    col = 0
    direction = 0

    total = n * (n + 1) // 2

    for number in range(1, total + 1):
        triangle[row][col] = number

        dr, dc = directions[direction]
        next_row = row + dr
        next_col = col + dc

        if (
            not (0 <= next_row < n and 0 <= next_col <= next_row)
            or triangle[next_row][next_col] != 0
        ):
            direction = (direction + 1) % 3

            dr, dc = directions[direction]
            next_row = row + dr
            next_col = col + dc

        row = next_row
        col = next_col

    answer = []

    for row in triangle:
        answer.extend(row)

    return answer