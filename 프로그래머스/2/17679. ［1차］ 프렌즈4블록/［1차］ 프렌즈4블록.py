def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]

    while True:
        deleted = set()

        for row in range(m - 1):
            for col in range(n - 1):
                block = board[row][col]

                if block is None:
                    continue

                same = True

                for direction in range(4):
                    next_row = row + dr[direction]
                    next_col = col + dc[direction]

                    if board[next_row][next_col] != block:
                        same = False
                        break

                if same:
                    for direction in range(4):
                        next_row = row + dr[direction]
                        next_col = col + dc[direction]

                        deleted.add((next_row, next_col))

        if not deleted:
            break

        answer += len(deleted)

        for row, col in deleted:
            board[row][col] = None

        for col in range(n):
            blocks = []

            for row in range(m):
                if board[row][col] is not None:
                    blocks.append(board[row][col])

            empty_count = m - len(blocks)

            for row in range(empty_count):
                board[row][col] = None

            for row in range(len(blocks)):
                board[empty_count + row][col] = blocks[row]

    return answer