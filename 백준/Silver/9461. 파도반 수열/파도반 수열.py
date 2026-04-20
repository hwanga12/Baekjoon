import sys
input = sys.stdin.readline

max_ = 100
ay = [0] * (max_ + 1)

ay[1], ay[2], ay[3], ay[4], ay[5] = 1, 1, 1, 2, 2

for i in range(6, max_ + 1):
    ay[i] = ay[i-1] + ay[i-5]

N = int(input())
for _ in range(N):
    j = int(input())
    print(ay[j])