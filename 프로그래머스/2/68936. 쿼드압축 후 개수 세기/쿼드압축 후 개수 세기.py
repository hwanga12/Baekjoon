def solution(arr):
    answer = [0, 0]
    n = len(arr)

    def check(row, col, size):
        first = arr[row][col]
        same = True

        for r in range(row, row + size):
            for c in range(col, col + size):
                if arr[r][c] != first:
                    same = False
                    break

            if not same:
                break

        if same:
            answer[first] += 1
            return

        half = size // 2

        check(row, col, half)                 
        check(row, col + half, half)      
        check(row + half, col, half)
        check(row + half, col + half, half)

    check(0, 0, n)

    return answer