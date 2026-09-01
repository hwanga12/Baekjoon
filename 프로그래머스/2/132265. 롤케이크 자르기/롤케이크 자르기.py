from collections import Counter

def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)

    for i in range(len(topping) - 1):
        left.add(topping[i])

        right[topping[i]] -= 1

        if right[topping[i]] == 0:
            del right[topping[i]]

        if len(left) == len(right):
            answer += 1

    return answer