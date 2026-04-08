import sys
input = sys.stdin.readline

N, M = map(int, input().split())

a = {}
for i in range(N):
    site, pwd = input().split()
    a[site] = pwd
for j in range(M):
    b = input().strip()
    print(a[b])