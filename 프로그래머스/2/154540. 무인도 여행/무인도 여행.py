# 아이디어 음. 유니온 파인드인가 그거 인가. 아니면 그냥 dfs로 전체 돌면서 할까. 
# 시간복잡도 100x100 ok
# 자료구조 dfs
import sys
sys.setrecursionlimit(100000)

def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    current = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
                
    def dfs(x, y):
        visited[x][y] = True
        total = int(maps[x][y])
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y    
            
            if not (0 <= nx < len(maps) and 0 <= ny < len(maps[0])):
                continue

            if maps[nx][ny] == 'X':
                continue
            
            if visited[nx][ny]:
                continue
                
            total += dfs(nx, ny)
        
        return total
        
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                island_sum = dfs(i, j)
                answer.append(island_sum)
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer