import heapq

def solution(book_time):
    def to_minutes(time):
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute

    book_time.sort()

    rooms = []

    for start, end in book_time:
        start = to_minutes(start)
        end = to_minutes(end) + 10

        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)

    return len(rooms)