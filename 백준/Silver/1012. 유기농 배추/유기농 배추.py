import sys
# 재귀 한도 늘리기 (필수)
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    # 상하좌우 네 방향 이동 좌표
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 현재 위치 방문 처리
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 지도 범위 내에 있고, 배추(1)가 있다면 계속 탐색
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    m, n, k = map(int, input().split()) # 가로, 세로, 배추 개수
    graph = [[0] * m for _ in range(n)]
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1 # 가로/세로 인덱스 주의

    worms = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1: # 배추 발견!
                dfs(i, j)
                worms += 1 # 구역 탐색 끝났으니 지렁이 추가
    print(worms)