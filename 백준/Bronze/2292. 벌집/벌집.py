N = int(input())

count = 1
max_room = 1

while N > max_room:
    max_room += 6 * count
    count += 1

print(count)