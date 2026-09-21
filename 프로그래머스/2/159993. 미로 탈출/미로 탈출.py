from collections import deque


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    start = None
    lever = None
    exit_point = None

    for x in range(rows):
        for y in range(cols):
            if maps[x][y] == "S":
                start = (x, y)
            elif maps[x][y] == "L":
                lever = (x, y)
            elif maps[x][y] == "E":
                exit_point = (x, y)

    def bfs(start, target):
        queue = deque()
        visited = [
            [False] * cols
            for _ in range(rows)
        ]

        start_x, start_y = start
        queue.append((start_x, start_y, 0))
        visited[start_x][start_y] = True

        while queue:
            x, y, distance = queue.popleft()

            if maps[x][y] == target:
                return distance

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and maps[nx][ny] != "X"
                    and not visited[nx][ny]
                ):
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))

        return -1

    distance_to_lever = bfs(start, "L")

    if distance_to_lever == -1:
        return -1

    distance_to_exit = bfs(lever, "E")

    if distance_to_exit == -1:
        return -1

    return distance_to_lever + distance_to_exit