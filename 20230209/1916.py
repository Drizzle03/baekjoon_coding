from sys import stdin
input = stdin.readline
import heapq
INF = int(1e9)

n = int(input()) #도시 개수
m = int(input()) #버스 개수

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dijkstra():
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1] #지금 거리 + 인접 그래프 거리
            if cost < distance[i[0]]:
                distance[i[0]] = cost #갱신
                heapq.heappush(q, (cost, i[0]))

dijkstra()
print(distance[end])