def solution(progresses, speeds):
    answer = []
    stack = []

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            stack.append((100 - progresses[i]) // speeds[i])
        else:
            stack.append((100 - progresses[i]) // speeds[i] + 1)

    current = 1

    for i in range(1, len(stack)):
        if stack[i] > stack[i-current]:
            answer.append(current)
            current = 1
        else:
            current += 1

    answer.append(current)

    return answer