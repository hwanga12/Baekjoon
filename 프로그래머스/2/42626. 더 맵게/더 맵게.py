import heapq


def solution(scoville, K):
    current = 0
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        current = first + second * 2

        heapq.heappush(scoville, current)
        answer += 1

    return answer