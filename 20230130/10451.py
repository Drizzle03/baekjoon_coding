from sys import stdin
from collections import deque
input = stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = True  #방문한 곳 1로 표시
    while queue:
        v = queue.popleft()
        next = graph[v]
        if not visited[next] : #아직 방문하지 않은 곳인 경우
            visited[next] = True
            queue.append(next)
    return 1

T = int(input())
for _ in range(T):
    answer = 0
    N = int(input())
    graph = [0] + list(map(int, input().split()))
    visited = [False] * (N + 1)

    for i in range(1, N+1):
        if not visited[i]:
            answer += bfs(i)
    print(answer) #순열 사이클의 개수
    



