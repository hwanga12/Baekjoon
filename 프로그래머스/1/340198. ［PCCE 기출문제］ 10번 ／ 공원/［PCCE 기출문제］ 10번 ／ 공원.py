def solution(mats, park):
    mats.sort(reverse=True)

    for size in mats:
        for i in range(len(park) - size + 1):
            for j in range(len(park[0]) - size + 1):

                possible = True

                for x in range(size):
                    for y in range(size):
                        if park[i + x][j + y] != "-1":
                            possible = False
                            break

                    if not possible:
                        break

                if possible:
                    return size

    return -1