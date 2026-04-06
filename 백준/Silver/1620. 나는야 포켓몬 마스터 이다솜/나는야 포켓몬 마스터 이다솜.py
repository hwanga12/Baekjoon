import sys

input = sys.stdin.readline

N, M = map(int, input().split())


a = {}
b = {}

for i in range(1, N + 1):
    word = input().strip()

    a[i] = word
    b[word] = i

for _ in range(M):
    query = input().strip()
    if query.isdigit():
        print(a[int(query)])
    else:
        print(b[query])