from sys import stdin

n = int(input()) 

new_li = []

for i in range(n):
    new_li.append(list(map(int, stdin.readline().split())))
    
cnt = n
need = 0
new_li = sorted(new_li, key=lambda new_li:(new_li[0],new_li[1]))

while len(new_li)!=0:
    if(cnt==0):
        break
    need +=1
    now = 0
    # 불가능 리스트 추출
    temp = new_li[:]
    new_li = []

    for i in range(len(temp)):
        if(temp[i][0] >= now):
            now = temp[i][1]
        else:
            new_li.append([temp[i][0],temp[i][1]])

print(need)