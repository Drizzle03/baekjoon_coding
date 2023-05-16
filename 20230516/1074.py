n, r, c = map(int, input().split())

# n : 격자 크기
# r : 행
# c : 열

# 재귀호출 횟수, 격자 크기, 찾고자 하는 열, 행
def zFuc(num, n, r, c):
    # 1. 찾고자 하는 열, 행이 어떤 분면에 해당하는가?

    idx = (2**n) / (2*num)
    print(idx) 
    #n이 2일 때, 4 / 2 * 1 = 2 
    #ary[0:2], 즉 0~idx-1까지가 2사분면

    #만약 횟수가 넘어간다면
    if idx < 1:
        print(0)
        return 0
    
    # 2 3 1
    #2사분면일 경우 : c 행 값이 idx보다 작고, r 열 값이 idx보다 작음 
    if r < idx and c < idx:
        v = (((2**n)/(2*num))**2) * 0 
        print(2)
        return v + zFuc(num+1, n, r, c)
    
    #1사분면일 경우 : r열 값이 idx보다 작고, c행 값이 idx보다 큼
    elif c >= idx and r < idx:
        v = (((2**n)/(2*num))**2) * 1 
        print(1)
        return v + zFuc(num+1, n, r, c)

    #3사분면일 경우 : c행 값이 idx보다 작고, r열 값이 idx보다 큼
    elif c < idx and r >= idx:
        v = (((2**n)/(2*num))**2) * 2 
        print(3, v-1)
        return v + zFuc(num+1, n, r, c)
    
    #4사분면일 경우 : c행 값이 idx보다 크거나 같고, r열 값이 idx보다 크거나 같음
    elif c >= idx and r >= idx:
        v = (((2**n)/(2*num))**2) * 3
        print(4, v)
        return v + zFuc(num+1, n, r, c)

print(zFuc(1, n, r, c))