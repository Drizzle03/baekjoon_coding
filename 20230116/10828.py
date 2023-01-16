from sys import stdin

n = int(stdin.readline())
stack = []
size = 0

for _ in range(n):
    command = list(map(str,stdin.readline().split()))

    if(command[0] == "push"):
        stack.append(int(command[1]))
        size +=1

    if(command[0] == "pop"):
        if (size <=0): print("-1")
        else:
            print(stack[size-1])
            del stack[size-1]
            size -=1
    if(command[0] == "size"):
        print(size)
    if(command[0] == "empty"):
        if(len(stack) > 0):
            print("0")
        else:
            print("1")
    if(command[0] == "top"):
        if(len(stack) == 0):
            print("-1")
        else:
            print(stack[size-1])
