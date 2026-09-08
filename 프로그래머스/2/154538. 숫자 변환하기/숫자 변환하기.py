from collections import deque


def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = {x}

    while queue:
        current, count = queue.popleft()

        if current == y:
            return count

        next_numbers = [
            current + n,
            current * 2,
            current * 3
        ]

        for next_number in next_numbers:
            if next_number <= y and next_number not in visited:
                visited.add(next_number)
                queue.append((next_number, count + 1))

    return -1