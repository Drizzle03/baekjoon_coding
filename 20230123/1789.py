S = int(input())
ans = 0
s = 0
for i in range(1,S+1):
    ans += 1
    s += i
    if(s > S):
        ans -=1
        break
print(ans)

    