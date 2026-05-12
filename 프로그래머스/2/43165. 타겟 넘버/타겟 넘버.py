
def solution(numbers, target):
    answer = 0
    return dfs(target, numbers,0, 0)
    
def dfs(target, numbers, current, sum_):

    if current == len(numbers):
        if sum_ == target:
            return 1  
        return 0      

    plus_case = dfs(target, numbers, current + 1, sum_ + numbers[current])
    
    minus_case = dfs(target, numbers, current + 1, sum_ - numbers[current])
    

    return plus_case + minus_case

