from collections import deque

def solution(priorities, location):
    answer = 0
    arr = deque()

    priorities = deque(enumerate(priorities))

    while len(priorities) > 0:
        if priorities[0][1] >= max(i[1] for i in priorities):
            ay = priorities.popleft()
            arr.append(ay)
            answer += 1

            if ay[0] == location:
                return answer
        else:
            priorities.append(priorities.popleft())

    return answer