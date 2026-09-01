from collections import deque

def solution(cacheSize, cities):
    answer = 0
    arr = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for i in cities:
        i = i.lower()

        if i in arr:
            answer += 1
            arr.remove(i)
        else:
            answer += 5

            if len(arr) >= cacheSize:
                arr.popleft()

        arr.append(i)

    return answer