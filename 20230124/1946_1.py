from sys import stdin
input = stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    ary = []

    for _ in range(N):
        a,b = map(int, input().split())
        ary.append([a,b])
    
    ary = sorted(ary, key=lambda ary:ary[0])

    new_ary = []
    new_ary.append([ary[0][0], ary[0][1]])
    for i in range(len(ary)):
        if ((ary[0][0] > ary[i][0]) or (ary[0][1] > ary[i][1])):
            new_ary.append([ary[i][0], ary[i][1]])

    new_ary = sorted(new_ary, key=lambda new_ary:new_ary[1])
    ans = 1

    nnew_ary = []
    nnew_ary.append([ary[0][0], ary[0][1]])
    for i in range(len(new_ary)):
        if (new_ary[0][0] > new_ary[i][0] or new_ary[0][1] > new_ary[i][1]):
            nnew_ary.append([ary[i][0], ary[i][1]])

    sum_ary = nnew_ary
    min_ary = 99999
    min_index = 0 

    #합이 작은 값 추출
    for i in range(len(sum_ary)):
        if(sum(sum_ary[i]) < min_ary):
            min_ary = sum(sum_ary[i])
            min_index = i
    
    ans = 1
    for i in range(len(nnew_ary)):
        if(nnew_ary[min_index][0] > nnew_ary[i][0] or nnew_ary[min_index][1] > nnew_ary[i][1]):
            ans +=1
    
    print(ans)