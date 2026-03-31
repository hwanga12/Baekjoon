A, B, V = map(int, input().split())
a = A - B

days = (V - A) // a

if (V - A) % a != 0:
    days += 1

print(days + 1)