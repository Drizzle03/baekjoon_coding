num = int(input())
li = list(map(int, input().split()))

for i in range(max(li)+1,max(li)*min(li)+1):
    check = 0
    for j in li:
        if(i % j != 0):
            check = 1
    if(check == 0): answer = i

print(answer)
