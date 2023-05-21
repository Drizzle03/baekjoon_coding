from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
bus_info = []

# 버스 정보 입력
for i in range(m):
    t, p = map(int, input().split())
    bus_info.append([t, p])

# 버스 대기열
bus_stop = [-1] * n

# 정차 중인 버스의 개수
bus_cnt = 0

# 영우가 타려는 버스의 인덱스
target_bus_idx = m - 1

# 시간 타이머
now_t = 0

while True:
    now_t += 1

    # 정차 중인 버스 처리
    for i in range(n):
        if bus_stop[i] != -1:
            bus_info[bus_stop[i]][1] -= 1
            if bus_info[bus_stop[i]][1] == 0:
                bus_stop[i] = -1
                bus_cnt -= 1

    if bus_cnt > 0:
        continue

    # 대기 중인 버스 처리
    for i in range(m):
        if bus_info[i][0] <= now_t:
            available_space = bus_stop.index(-1)
            if available_space != -1:
                bus_stop[available_space] = i
                bus_cnt += 1

    # 영우가 타려는 버스의 정차 위치를 찾음
    if bus_stop.count(-1) == n:
        print(target_bus_idx + 1)
        break
