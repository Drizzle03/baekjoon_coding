from sys import stdin
input = stdin.readline
from collections import deque

#
st = list(input())
left_stack = deque(st[:-1])
right_stack = deque([])

m = int(input())
n = len(st[:-1])

cs = n
for _ in range(m):
    cmd = list(map(str, input().split()))
    #커서 왼쪽 문자 추가
    if cmd[0] == 'P':
        left_stack.append(cmd[1])
        cs+=1

    #커서 왼쪽 이동
    elif cmd[0] == 'L':
        if len(left_stack):
            temp = left_stack.pop()
            right_stack.appendleft(temp)
            cs -=1
    
    #커서 왼쪽 문자 삭제
    elif cmd[0] == 'B':
        if cs != 0:
            left_stack.pop()
            cs -=1
    
    #커서 오른쪽 이동
    elif cmd[0] == 'D':
        if len(right_stack):
            temp = right_stack.popleft()
            left_stack.append(temp)
            cs +=1

print("".join(left_stack)+"".join(right_stack))