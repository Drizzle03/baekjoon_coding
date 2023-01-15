ip = list(map(int, input().split()))
goal = [1,1,2,2,2,8]
op = [0]*6

for i in range(6):
    if(ip[i]==goal[i]): op[i] = 0
    else: op[i] = goal[i] - ip[i]

print(op[0], op[1], op[2], op[3], op[4], op[5])