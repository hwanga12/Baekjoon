def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 == 1:
                arr[i] += n
    else:
        if len(arr) % 2 == 1:
            for j in range(len(arr)):
                if j % 2 == 0:
                    arr[j] += n
            
    return arr