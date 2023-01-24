from collections import deque
ip  = list(map(str, input().split()))

#공통인자, 세미콜론 제거
com = ip[0]
l = len(ip)
ip[l-1] = ip[l-1][:-1]
ip = ip[1:]

for i in ip:
    li = deque()
    li.append(i)

    op = deque()
    value = ''

    for j in i:
        if(j=='*' or j=='[' or j==']'or j=='&' or j==','):
            if(j=='['):
                op.append(']')
            elif (j==']'):
                op.append('[')
            elif(j=='*' or j=='&'):
                op.append(j)
            else:
                pass
        else:
            value += j

    op.reverse()
    out = list(op)
    out = ''.join(s for s in out)
    print(com+out,value+';')