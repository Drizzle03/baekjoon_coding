from collections import deque
from sys import stdin
input = stdin.readline

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True #방문 처리
    print(v, end= ' ') #출력
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 입력
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(m):
    graph[i].sort()

print(graph)

# dfs(graph, v, visited)
# visited = [False] * (n+1)
# print()
# bfs(graph, v, visited)
