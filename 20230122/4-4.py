from sys import stdin

sizex, sizey = map(int, input().split())
nowposx, nowposy, way = map(int, input().split())

land = []
for i in range(sizex):
    land.append(list(map(int, stdin.readline().split())))

print(land)