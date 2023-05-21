from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
bus_info = []

# bus info input
for i in range(m):
    t, p = map(int, input().split())
    bus_info.append([t, p])

# 버스 대기열, 버스 id 입력 
bus_stop = [-1 for _ in range(n)]

# 정차 버스 중 마지막 버스의 idx
idx = -1

# 정차 중인 버스의 갯수
bus_cnt = 0

# 시간 타이머
now_t = 0
while True:
    now_t +=1
    # print(now_t)

    if idx >= m-1: #2
        print(bus_stop.index(m-1)+1)
        # print(bus_stop)
        break

    # 정차중인 버스가 있다면 
    if bus_cnt > 0:
        for i in range(len(bus_stop)): # 0 - 1
            #정차 버스 중 정차 시간 감소
            if bus_stop[i] != -1:
                #정차 버스의 시간 감소
                bus_info[bus_stop[i]][1] -= 1
            
                #만약 정차 시간이 지났고
                if bus_info[bus_stop[i]][1] == 0:

                    # 앞에 모두 차가 없다면
                    for j in bus_info[:bus_stop[i]]:
                        # print(now_t, bus_cnt, bus_info)
                        if j != -1:
                            break
                    else: #버스 빼줌
                        bus_stop[i] = -1
                        bus_cnt -= 1
            

    #정차 버스 공간이 있다면
    if bus_stop[-1] == -1:
        # 이전 정차 버스 이후 버스 돌려봄
        for i in range(idx+1, m): # 2 - 2
            # 현재 시간보다 같거나 작다면
            if now_t >= bus_info[i][0]:
                # 공간을 찾음
                space = len(bus_stop) -1 #1
                for j in range(len(bus_stop)-1, -1, -1): #1-0
                    #빈 공간을 찾으면 업데이트
                    if bus_stop[j] == -1:
                        space = j
                    #다른 버스가 정차 중이라면 멈춤
                    else:
                        break
                # 대기열의 빈 공간에 i번째 버스 삽입
                bus_stop[space] = i
                idx = i
                bus_cnt += 1


