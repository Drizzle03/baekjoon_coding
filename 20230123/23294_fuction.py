import sys
from collections import deque

N, Q, C = map(int, sys.stdin.readline().split())
caps = list(map(int, sys.stdin.readline().split()))

usingcash = 0
back, front = deque(), deque() #back 덱, front 덱
nowpage = 0 #now page

# 뒤로가기
def backward(page):
    if len(back) == 0:
        return page

    front.appendleft(page)
    now = back.popleft()

    return now

def frontward(page):
    if len(front) == 0:
        return page

    back.appendleft(page)
    now = front.popleft()

    return now

def access(page, next, cash, flag):
    cash -= sum([caps[f-1] for f in front])
    front.clear()

    now = next
    cash += caps[now-1]

    if flag and page != 0:
        back.appendleft(page)
        
        while cash > C:
            cash -= caps[back.pop()-1]

    return now, cash

def compress(cash):
    tmplist = deque()

    for b in back:
        if len(tmplist) == 0 or tmplist[-1] != b:
            tmplist.append(b)
        else:
            cash -= caps[b-1]
    
    return cash, tmplist

flag = False
for i in range(Q):
    command = sys.stdin.readline().split()

    if command[0] == 'B':
        nowpage = backward(nowpage)

    elif command[0] == 'F':
        nowpage = frontward(nowpage)

    elif command[0] == 'A':
        nowpage, usingcash = access(nowpage, int(command[1]), usingcash, flag)
        if flag == False:
            flag = True

    else:
        usingcash, back = compress(usingcash)

    

print(nowpage)
print(*back) if back else print(-1)
print(*front) if front else print(-1)