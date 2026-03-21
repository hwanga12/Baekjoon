import sys
input = sys.stdin.readline

n, m = map(int, input().split())
res = []

def backtracking(st):
    if len(res) == m:	#종료조건
        return print(' '.join(map(str, res)))

    for i in range(st, n+1):
        res.append(i)
        backtracking(i)
        res.pop()

backtracking(1)