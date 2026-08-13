def solution(n, w, num):
    boxes = [[] for _ in range(w)]

    for i in range(1, n + 1):
        floor = (i - 1) // w
        pos = (i - 1) % w

        # 짝수 층(0, 2, 4...)은 왼쪽 → 오른쪽
        if floor % 2 == 0:
            col = pos
        # 홀수 층은 오른쪽 → 왼쪽
        else:
            col = w - 1 - pos

        boxes[col].append(i)

    for col in boxes:
        if num in col:
            index = col.index(num)
            return len(col) - index