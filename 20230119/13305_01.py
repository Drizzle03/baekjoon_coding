N = int(input()) #도시의 개수
length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
length.append(0)

c_oil = 0
c_price = 0
min_v = min(oil_price[:N-1]) #기름 가장 싼 곳
sum_price = sum(length) #필요한 기름의 총 리터

for i in range(N):
    #제일 저렴한 곳에 도착 했다면
    if(oil_price[i] == min_v and c_oil < (sum_price - sum(length[:i]))):
        c_oil += sum_price - sum(length[:i]) #앞으로 더 가야하는 거리만큼 오일 충전
        c_price += oil_price[i]*(sum_price - sum(length[:i]))

    if(i<N-1):
        #이번 주유소 기름이 다음 주유소보다 저렴하고, 다음 주유소까지 갈 기름이 없다면
        if(oil_price[i] <= oil_price[i+1] and c_oil < (length[i]+length[i+1])):
            c_oil += length[i]+length[i+1]
            c_price += oil_price[i]*(length[i]+length[i+1])
            c_oil -= length[i]
            #오일이 다음 도시로 갈 수 있을 만큼 남아있다면
        elif(c_oil >= length[i]): #다음 주유소보다 저렴하지 않지만, 기름이 충분히 있다면
            c_oil -= length[i]

        else: #기름이 부족하다면
            c_oil += length[i]
            c_price += oil_price[i]*length[i]
            c_oil -= length[i]

print(c_price)