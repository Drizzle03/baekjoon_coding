from collections import deque
from sys import stdin
input = stdin.readline

def bfs(virus):
    queue = deque([virus])
    visited[virus] = True
    
    while (len(queue)!=0):
        v = queue.popleft()
        visited[v] = True

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)

c_num = int(input())
n = int(input())

visited = [False]*(c_num+1)
graph = [[] for _ in range(c_num+1)]

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(visited.count(True) -1 )
