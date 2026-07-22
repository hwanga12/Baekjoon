def solution(arr):
    answer = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    for target in answer:
        if len(arr) <= target:
            arr.extend([0] * (target - len(arr)))
            return arr