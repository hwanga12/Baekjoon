from collections import deque

def solution(s):
    def good(arr):
        stack = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in arr:
            if bracket in '([{':
                stack.append(bracket)
            else:
                if not stack or stack[-1] != pair[bracket]:
                    return False
                stack.pop()

        return len(stack) == 0

    arr = deque(s)
    answer = 0

    for _ in range(len(s)):
        if good(arr):
            answer += 1

        arr.rotate(-1)

    return answer