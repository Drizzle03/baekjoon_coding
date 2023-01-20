n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

res = 0
m = costs[0]
for i in range(n-1):
    #지금 비용이 최솟값보다 작다면 갱신
    if costs[i] < m:
        m = costs[i]

    #최솟값이든 뭐든 결과가 어떻든 res값에 m * roads를 더함
    res += m * roads[i]
print(res)