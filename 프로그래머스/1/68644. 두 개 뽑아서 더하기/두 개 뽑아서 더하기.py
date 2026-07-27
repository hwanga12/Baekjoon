from itertools import combinations

def solution(numbers):
    answer = []

    for pair in combinations(numbers, 2):
        answer.append(sum(pair))

    return sorted(set(answer))