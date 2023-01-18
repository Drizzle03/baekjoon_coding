# 그리디 문제 2
from sys import stdin

N = int(stdin.readline())
li = [] #start, end, time
cnt = 0
max = 0
#회의 시간, 인덱스

for i in range(N):
    li.append(list(map(int, stdin.readline().split()))) #start, end
    li[i].append(li[i][1] - li[i][0]) #회의 시간
    if(li[i][1] > max): max = li[i][1]
li.sort(key=lambda li:li[2]) #2번 인덱스 값 기준 정렬

status = [0]*(max+1)

for start, end, time in li:
    if(time == 0):
        if(status[start] != 1):
            status[start] = 1
            cnt+=1

    elif(status[start:end] == [0]*time): #만약 status가 모두 0이라면
        status[start:end] = [1]*time
        cnt+=1

print(cnt)