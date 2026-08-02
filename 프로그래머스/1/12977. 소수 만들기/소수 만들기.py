import math
from itertools import combinations

def solution(nums):
    answer = 0
    ay = []
    
    for i in combinations(nums, 3):
        ay.append(sum(i))
    
    print(ay)
    
    for p in ay:
        is_prime = True

        for q in range(2, int(math.sqrt(p)) + 1):
            if p % q == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1

    return answer
