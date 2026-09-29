from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for size in course:
        counter = Counter()

        for order in orders:
            if len(order) < size:
                continue

            for comb in combinations(sorted(order), size):
                menu = "".join(comb)
                counter[menu] += 1

        
        ay = max(counter.values())
        
        if ay >= 2:
            for menu, count in counter.items():
                if count == ay:
                    answer.append(menu)
        
        
    return sorted(answer)