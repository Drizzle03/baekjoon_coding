import heapq
INF = int(1e9)

M, N = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
distance = [[INF] * M for _ in range(N)]

dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]  # 상 우 하 좌


def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        cost, x, y = heapq.heappop(q)

        if cost > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어나기 방지 and 방문한 적 있으면 무시
                continue
            
            # 현재 루트의 비용이 작다면, 갱신
            if cost + arr[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = cost + arr[nx][ny]
                # 힙 추가
                heapq.heappush(q, (distance[nx][ny], nx, ny))

dijkstra()
print(distance[N - 1][M - 1])