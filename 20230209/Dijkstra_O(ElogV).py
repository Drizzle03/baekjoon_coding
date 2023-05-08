import heapq
from sys import stdin

input = stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력
n,m = map(int, input().split())
#시작 노드 입력
start = int(input())
graph = [[] for _ in range(n+1)] # 연결 정보 리스트
visited = [False]*(n+1) # 방문 여부 리스트
distance = [INF] * (n+1) # 최단거리 리스트

# 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) #a에 b연결, c만큼의 거리 가짐

def dijkstra():
    q = []
    heapq.heappush(q, (0, start)) #거리, 노드 번호
    visited[start] = True #start 방문 처리
    distance[start] = 0

    while q:
        # 최단거리 꺼냄
        dist, now = heapq.heappop(q)
        
        # 해당 인덱스의 
        if distance[now] < dist:
            continue
        
        # 인접한 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1] #거리 = 현재 노드까지의 거리 + 인접한 다른 노드의 거리
            if cost < distance[i[0]]: #총 비용이 기존에 저장된 최단거리보다 작다면
                distance[i[0]] = cost #최단거리에 현재 총 비용 갱신
                heapq.heappush(q, (cost,i[0])) #갱신된 내용을 push

dijkstra()

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])