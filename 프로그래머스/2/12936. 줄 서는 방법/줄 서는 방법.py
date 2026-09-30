from math import factorial

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    k -= 1

    for remain in range(n, 0, -1):
        block_size = factorial(remain - 1)
        index, k = divmod(k, block_size)
        answer.append(numbers.pop(index))

    return answer