from math import gcd

def solution(signals):
    limit = 1

    for green, yellow, red in signals:
        cycle = green + yellow + red
        limit = limit * cycle // gcd(limit, cycle)

    for t in range(1, limit + 1):
        all_yellow = True

        for green, yellow, red in signals:
            cycle = green + yellow + red
            pos = (t - 1) % cycle

            if not (green <= pos < green + yellow):
                all_yellow = False
                break

        if all_yellow:
            return t

    return -1