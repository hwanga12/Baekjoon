def solution(n):
    answer = 0
    a = bin(n).count('1')
    
    b = n + 1
    while True:
        if bin(b).count('1') == a:
            return b
        b += 1