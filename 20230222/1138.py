n = int(input())
li = list(map(int, input().split()))

chk = [0]*n
for i in range(len(li)):
    cnt = 0
    idx = 0
    for j in range(len(li)):
        if chk[j] == 0:
            cnt +=1
            idx = j
        if (cnt-1) == li[i]:
            chk[idx] = i+1
print(*chk)


