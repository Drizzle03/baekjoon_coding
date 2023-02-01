# 풀이 중도 포기 (2/1 이어서 시도)

from collections import deque
from sys import stdin

input = stdin.readline

def dfs(h, w):
    queue = deque([h, w])
    visited[h, w] = True

    for i, j in li[h]:
        if not visited[j]:
            pass

h, w = map(int, input().split())
li = []

res = 0
max = 0

# 육지 바다 정보 입력
for _ in range(h):
    li.append(list(map(str, input().split())))

for i in range(h):
    for j in range(w):
        if li[i][j] == 'L': #육지라면 bfs 탐색 돌림
            visited = [[False]*w]*h
            res = bfs(i, j)
            if res > max:
                max = res

print(res)

