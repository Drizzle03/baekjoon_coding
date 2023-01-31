from collections import deque
from sys import stdin
input = stdin.readline

# O(N)
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 입력
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*(N+1)
ans = 0

# bfs 적용
for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]:
            ans +=1
            visited[i] = True
        else:
            bfs(i)
            ans +=1

print(ans)