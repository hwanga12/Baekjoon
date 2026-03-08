import sys
from collections import deque

# 1. 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# N: 정점 개수, M: 간선 개수, V: 시작 정점
N, M, V = map(int, input().split())

# 2. 인접 리스트 생성 (1번 노드부터 사용하므로 N+1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u) # 양방향 연결

# 3. 방문 번호가 낮은 순으로 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS 함수 (재귀 방식)
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# BFS 함수 (deque 활용)
def bfs(v):
    visited = [False] * (N + 1)
    queue = deque([v])
    visited[v] = True
    
    while queue:
        curr = queue.popleft() # deque의 popleft는 O(1)
        print(curr, end=' ')
        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 4. 결과 출력
dfs_visited = [False] * (N + 1)
dfs(V, dfs_visited)
print() # 줄바꿈
bfs(V)