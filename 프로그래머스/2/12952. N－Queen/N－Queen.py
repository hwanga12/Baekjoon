def solution(n):
    answer = 0

    used_col = set()
    used_diagonal1 = set()
    used_diagonal2 = set()

    def dfs(row):
        nonlocal answer

        if row == n:
            answer += 1
            return

        for col in range(n):
            if col in used_col:
                continue

            if row - col in used_diagonal1:
                continue

            if row + col in used_diagonal2:
                continue
            
            used_col.add(col)
            used_diagonal1.add(row - col)
            used_diagonal2.add(row + col)

            dfs(row + 1)

            used_col.remove(col)
            used_diagonal1.remove(row - col)
            used_diagonal2.remove(row + col)

    dfs(0)

    return answer