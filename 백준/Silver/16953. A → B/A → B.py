import sys

A, B = map(int, sys.stdin.readline().split())
count = 1

while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B //= 10
    else:
        break
    count += 1

if B == A:
    print(count)
else:
    print(-1)