import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

# 1. 입력 받기
N, M = map(int, input().split())
# 중복된 숫자가 들어올 수 있으므로 set으로 중복 제거 후 정렬
arr = sorted(list(set(map(int, input().split()))))

# 2. 중복 조합 생성 (M개를 뽑음)
# combinations_with_replacement는 이미 정렬된 arr에서
# 중복을 허용하여 비내림차순으로 뽑아줍니다.
results = combinations_with_replacement(arr, M)

# 3. 결과 출력
for res in results:
    print(*res)