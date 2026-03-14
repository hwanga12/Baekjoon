import sys
from itertools import permutations

# 1. 입력 받기
input = sys.stdin.read().split()
n, m = int(input[0]), int(input[1])
numbers = sorted(list(map(int, input[2:]))) # 입력과 동시에 정렬

# 2. 순열 생성 (n개 중 m개를 뽑는 모든 경우)
# permutations는 튜플 형태의 이터레이터를 반환합니다.
result = permutations(numbers, m)

# 3. 결과 출력
for p in result:
    print(*(p))