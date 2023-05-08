from sys import stdin
input = stdin.readline
import heapq
INF = int(1e9)

v,e = map(int, input().split())
start = int(input())

# 간선 노드 기록
graph = [[] for _ in range(v+1)]
# 최단거리 기록
distance = [INF] * (v+1) 

# 큐
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #인접 노드, 거리 기록


def dijkstra():
    q = []
    heapq.heappush(q, (0, start)) #거리 시작 노드 입력
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 현재 거리가 dist보다 작다는 것 == 이미 처리된 적이 있다는 것, 계속 쌓이니까!
        if distance[now] < dist:
                continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 최단거리에 삽입
dijkstra()

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])