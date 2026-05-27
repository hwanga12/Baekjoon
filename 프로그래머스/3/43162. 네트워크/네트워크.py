from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    queue = deque()
    
    
    for i in range(n):
         if not visited[i]:
                visited[i] = True
                queue.append(i)
                
                while queue:
                    now = queue.popleft()
                    for j in range(n):
                        if not visited[j] and computers[now][j] == 1:
                            visited[j] = True
                            queue.append(j)
                answer += 1
    
    
    return answer