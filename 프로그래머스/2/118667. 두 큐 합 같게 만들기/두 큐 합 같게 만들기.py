from collections import deque


def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)

    total = sum1 + sum2

    if total % 2 == 1:
        return -1


    limit = (len(q1) + len(q2)) * 2

    while answer <= limit:
        if sum1 == sum2:
            return answer

        
        if sum1 > sum2:
            value = q1.popleft()
            q2.append(value)

            sum1 -= value
            sum2 += value

        else:
            value = q2.popleft()
            q1.append(value)

            sum2 -= value
            sum1 += value

        answer += 1

    return -1