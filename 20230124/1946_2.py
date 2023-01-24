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

    ans = 1
    std = ary[0][1]
    for i in range(N):
        if(std > ary[i][1]):
            ans+=1
            std = ary[i][1]
    print(ans)