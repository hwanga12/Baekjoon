from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 4방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # BFS를 위한 큐 생성 및 시작점(0, 0) 삽입
    queue = deque()
    queue.append((0, 0))
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4방향으로 물결 퍼뜨리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵을 벗어났거나, 벽(0)을 만나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
                
            # 아직 안 가본 길(1)이라면
            if maps[nx][ny] == 1:
                # ★ 핵심: 이전 칸까지 온 거리에 + 1을 해서 내 칸에 적어둔다!
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    # 도착점(우측 하단)의 값이 1보다 크면 도달 성공 (최단 거리)
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    # 도착점이 여전히 1이라면(또는 벽에 막혀서 못 갔다면) 도달 실패
    else:
        return -1