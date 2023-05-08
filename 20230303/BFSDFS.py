from collections import deque
from sys import stdin
input = stdin.readline

def dfs(v):
    visited[v] = True #현 위치 True
    print(v, end= ' ')

    for i in graph[v]:
        if not visited[i]: #방문 x라면
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(v)
print()
visited = [False]*(n+1)
bfs(v)