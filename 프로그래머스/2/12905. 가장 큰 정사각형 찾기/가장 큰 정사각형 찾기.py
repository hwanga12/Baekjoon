def solution(board):
    max_size = 0

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == 1:
                if i > 0 and j > 0:
                    board[i][j] = min(
                        board[i - 1][j],
                        board[i][j - 1],
                        board[i - 1][j - 1]
                    ) + 1

                max_size = max(max_size, board[i][j])
    return max_size * max_size