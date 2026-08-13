def solution(friends, gifts):
    n = len(friends)

    # 이름 -> 번호
    idx = {}

    for i in range(n):
        idx[friends[i]] = i

    # gift[a][b] = a가 b에게 준 선물 개수
    gift = [[0] * n for _ in range(n)]

    # 선물 지수 = 준 개수 - 받은 개수
    score = [0] * n

    # 다음 달에 받을 선물 개수
    answer = [0] * n

    # 지금까지 선물 기록 정리
    for g in gifts:
        giver, receiver = g.split()

        a = idx[giver]
        b = idx[receiver]

        gift[a][b] += 1

        # 준 사람은 +1
        score[a] += 1

        # 받은 사람은 -1
        score[b] -= 1

    # 친구 두 명씩 비교
    for i in range(n):
        for j in range(i + 1, n):

            # i가 j에게 더 많이 줌
            if gift[i][j] > gift[j][i]:
                answer[i] += 1

            # j가 i에게 더 많이 줌
            elif gift[i][j] < gift[j][i]:
                answer[j] += 1

            # 서로 준 횟수가 같음
            else:
                # 선물 지수 비교
                if score[i] > score[j]:
                    answer[i] += 1

                elif score[i] < score[j]:
                    answer[j] += 1

    return max(answer)