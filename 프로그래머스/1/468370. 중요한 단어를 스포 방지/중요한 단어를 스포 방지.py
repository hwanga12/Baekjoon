def solution(message, spoiler_ranges):
    normal = set()
    spoiler = set()

    word_info = []
    idx = 0

    # 단어별 실제 시작/끝 위치 저장
    for word in message.split():
        start = message.find(word, idx)
        end = start + len(word) - 1

        word_info.append((word, start, end))

        idx = end + 1

    # 한 번만 순회
    for word, start, end in word_info:
        is_spoiler = False

        # 이 단어가 스포 구간과 겹치는지 확인
        for s, e in spoiler_ranges:
            if start <= e and s <= end:
                is_spoiler = True
                break

        if is_spoiler:
            # 일반 영역에서 나온 적 없으면 중요한 단어 후보
            if word not in normal:
                spoiler.add(word)

        else:
            # 일반 영역에 등장한 단어
            normal.add(word)

            # 이전에 스포 후보였어도 일반에 등장했으므로 제거
            spoiler.discard(word)

    return len(spoiler)