#r행, c열
n, r, c = map(int, input().split())

def rec(num, n, y, x):
    #호출 횟수, 열, 행
    
    #사분면 위치 확인
    idx = 2**n / (2*num)

    #2사분면
    if x >= 0 and x <= idx and y >= 0 and y <= idx:
        return ((2**n / num*2) ** 2) * 0 + rec(num+1, n, y, x)
    
    #1사분면
    elif x > idx and x <= idx*2 and y >=0 and y <= idx:



rec(0, n, r, c)