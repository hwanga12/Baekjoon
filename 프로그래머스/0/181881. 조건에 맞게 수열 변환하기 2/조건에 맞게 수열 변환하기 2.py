def solution(arr):
    count = 0

    while True:
        prev = arr[:]

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] //= 2
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1

        if prev == arr:
            return count

        count += 1