N = int(input())
ans = 0
check = 0
while(N>=0):
    if(N%5==0):
        ans += (N//5)
        print(ans)
        check = 1
        break
    N -= 3
    ans +=1

if(check == 0): print(-1)

