n=int(input())
dp=[0]*(n+3)
dp[1],dp[2],dp[3]=0,1,1

for i in range(4,n+1):

    # 2와 3 모두 나뉘어 떨어질 경우,
    # 3로 나누는 것, 2로 나누는 것, 1을 빼는 것 중 어떤 게 더 숫자가 작은지
    if i%2==0 and i%3==0:
        dp[i]=min(dp[i//3],dp[i//2],dp[i-1])+1
    
    # 3으로만 나누어 떨어질 경우
    # 3을 나누는 것, 1을 빼는 것 중 어떤 것이 더 작은지
    elif i%3==0:
        dp[i] = min(dp[i // 3],dp[i-1]) + 1

    elif i%2==0:
        dp[i] = min(dp[i // 2],dp[i-1]) + 1
    else:
        dp[i]=dp[i-1]+1

print(dp[n])