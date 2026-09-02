def solution(dirs):
    visited = set()

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    direction = {
        "R": 0,
        "L": 1,
        "D": 2,
        "U": 3
    }

    x, y = 0, 0

    for command in dirs:
        index = direction[command]

        nx = x + dx[index]
        ny = y + dy[index]

        
        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            continue

        edge = tuple(sorted(((x, y), (nx, ny))))
        visited.add(edge)

        x, y = nx, ny

    return len(visited)