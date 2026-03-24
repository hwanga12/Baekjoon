import sys
input = sys.stdin.readline


N = int(input())
a = list(map(int, input().split()))
sorted_a = sorted(a)
current_ = 0
result = 0
for i in sorted_a: 
    current_ += i
    result += current_

print(result)
