from itertools import permutations
def solution(numbers):
    answer = 0
    nums = set()
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            nums.add(int(''.join(j)))
    
    for n in nums:
        if n < 2:
            continue
        
        prime = True
        
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            answer += 1
    return answer