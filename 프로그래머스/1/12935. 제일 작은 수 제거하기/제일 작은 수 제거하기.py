def solution(arr):
    answer = []
    ay = [-1]
    arr.remove(min(arr))
    if len(arr) == 0:
        return ay 
    else:
        return arr