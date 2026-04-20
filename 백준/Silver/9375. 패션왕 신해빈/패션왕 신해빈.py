import sys

# 딕셔너리는 없는 키에 갑자기 값을 더하거나 추가하려고 하면 keyError가 발생함. 따라서 항상 키가 존재하는지 확인해야 함.
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        item_name, category = input().split()
        clothes[category] += 1

    answer = 1

    for count in clothes.values():
        answer *= (count + 1)

    print(answer - 1)