from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    queue = deque([(0, 0)])
    visited = [[False] * cols for _ in range(rows)]
    visited[0][0] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if x == rows - 1 and y == cols - 1:
            return maps[x][y]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < rows
                and 0 <= ny < cols
                and maps[nx][ny] == 1
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return -1