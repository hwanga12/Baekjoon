def solution(players, callings):
    rank = {}

    # 이름 → 현재 인덱스
    for i in range(len(players)):
        rank[players[i]] = i

    for name in callings:
        current_index = rank[name]
        front_index = current_index - 1

        front_player = players[front_index]

        # 실제 선수 배열에서 자리 교환
        players[front_index], players[current_index] = (
            players[current_index],
            players[front_index]
        )

        # 딕셔너리의 인덱스도 갱신
        rank[name] = front_index
        rank[front_player] = current_index

    return players