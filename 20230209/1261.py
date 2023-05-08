from sys import stdin
input = stdin.readline
import heapq
INF = int(1e9)

n, m = map(int, input().split())
wall = [[]]
breakwall = [[INF] * m for _ in range(n)]
wall = [list(map(int, input())) for _ in range(n)]


move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
start = [1,1]

q = []
heapq.heappush(q, (0, start[0], start[1]))
breakwall[start[0]][start[1]] = 0

while q:
    brwa, nowx, nowy = heapq.heappop(q)
    if breakwall[nowx][nowy] < brwa:
        continue

    for mo in move:
        if (nowx + mo[0]) <= n and (nowx + mo[0]) > 0 and (nowy + mo[1]) > 0 and (nowy + mo[1]) <= m:
            x = nowx+mo[0] 
            y = nowy+mo[1]
            if(wall[x][y] == '1'): cost = brwa + 1
            else: cost = brwa
            if cost < breakwall[x][y]:
                breakwall[x][y] = cost
                heapq.heappush(q, (cost, x, y))

print(breakwall[n][m])


