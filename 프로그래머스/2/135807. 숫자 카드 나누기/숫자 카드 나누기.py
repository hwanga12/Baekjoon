from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    answer = 0

    # gcdA가 B의 어떤 숫자도 나누지 못하는지 확인
    if all(num % gcdA != 0 for num in arrayB):
        answer = max(answer, gcdA)

    # gcdB가 A의 어떤 숫자도 나누지 못하는지 확인
    if all(num % gcdB != 0 for num in arrayA):
        answer = max(answer, gcdB)

    return answer