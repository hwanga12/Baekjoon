from collections import deque

def solution(arr):
    answer = []
    current = -1
    for i in range(len(arr)):
        if current != arr[i]:
            answer.append(arr[i])
            current = arr[i]
    return answer