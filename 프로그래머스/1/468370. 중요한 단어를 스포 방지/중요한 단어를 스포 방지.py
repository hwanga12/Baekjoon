def solution(message, spoiler_ranges):
    words = message.split()

    normal = set()
    spoiler = set()

    idx = 0
    word_info = []

    # 단어별 위치 저장
    for word in words:
        start = message.find(word, idx)
        end = start + len(word) - 1

        word_info.append((word, start, end))

        idx = end + 2

    # 1. 스포가 아닌 단어만 normal에 저장
    for word, start, end in word_info:
        is_spoiler = False

        for s, e in spoiler_ranges:
            if start <= e and s <= end:
                is_spoiler = True
                break

        if not is_spoiler:
            normal.add(word)

    # 2. 스포 단어 중 normal에 없는 것만 저장
    for word, start, end in word_info:
        for s, e in spoiler_ranges:
            if start <= e and s <= end:
                if word not in normal:
                    spoiler.add(word)
                break

    return len(spoiler)