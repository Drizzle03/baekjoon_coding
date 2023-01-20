N = int(input()) #도시의 개수
l = list(map(int, input().split())) #거리
oil = list(map(int, input().split())) #오일 가격

total = oil[0]*l[0] #1 -> 2 도시 가는 비용
now = 1
min_oil = min(oil[:N-1]) #기름 가장 싼 곳


#1 -> 2 -> 3 -> 4 

while True:
    # 만약 현재 도시의 오일이 다음 도시보다 더 싸다면
    # 이번 시티 -> 다음 시티 -> 다다음 시티까지 기름 구매
    if(now >= N-1):
        break
    
    if(oil[now]==min_oil):
        total += oil[now] * (sum(l[now:]))
        break
    
    if(oil[now] < oil[now+1]):
        total += oil[now] * (l[now]+l[now+1])
        now += 2
    else:
        total += oil[now]*l[now]
        now += 1

print(total)