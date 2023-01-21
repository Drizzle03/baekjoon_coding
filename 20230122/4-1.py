def outline(x, y, n):
    if(x > 0 and x <= N and y>0 and y<= n):
        return True
    else:
        return False

N = int(input())
# m = [[0] * N]*N

command = list(map(str, input().split()))
pos = [1, 1]
print(command)

for i in range(len(command)):
    if(command[i] == "L"):
        if outline(pos[0] , pos[1]-1, N):
            pos[1] -= 1
    if(command[i] == "R"):
        if outline(pos[0] , pos[1]+1, N):
            pos[1]+= 1
    if(command[i] == "U"):
        if outline(pos[0]-1, pos[1], N):
            pos[0] -= 1
    if(command[i] == "D"):
        if outline(pos[0]+1 , pos[1], N):
            pos[0] += 1
    print(i, pos[0],pos[1])

print(pos[0], pos[1])