from math import lcm

def solution(arr):
    answer = arr[0]

    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer