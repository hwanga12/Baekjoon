from collections import deque

def solution(maps):
    
    queue = deque()
    queue.append((0, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(maps)
    m = len(maps[0])
    
    
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maps[ny][nx] == 0:
                continue
            
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x]+ 1
                queue.append((ny, nx))
                
    if maps[n-1][m-1] > 1:
        return maps[n-1][m-1]
    elif maps[n-1][m-1] == 1:
        return -1