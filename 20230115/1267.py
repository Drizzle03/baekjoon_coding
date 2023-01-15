from sys import stdin
n = int(stdin.readline())
m = list(map(int, stdin.readline().split()))
fare = [0,0]

for i in m:
    fare[0] += (i//30)*10
    if((i%30)>=0): fare[0] += 10
    
    fare[1] += (i//60)*15
    if((i%60)>=0): fare[1] += 15

if(fare[0] < fare[1]): print("Y", fare[0])
elif(fare[0] == fare[1]): print("Y M", fare[0])
else: print("M",fare[1])
