T = int(input())
for i in range(1, T+1):
    x, y = map(int, input().split())
    
    a = x - y
    b = 2*y -x
    print(f'#{i} {b} {a}')

