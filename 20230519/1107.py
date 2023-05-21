from sys import stdin
input = stdin.readline

N = int(input()) # 목표 채널 
M = int(input()) # 고장난 버튼 갯수

# 고장난 버튼 번호들
btn_li = list(map(int, input().split()))

ans = 9999999999999

if btn_li:
    for num in range(1000000):
        # 고장난 버튼들로 만들 수 있다
        for i in str(num):
            if i in btn_li:
                break     
        else:
            #목표채널 - 지금 현재값
            ans = min(abs(N - num), ans)
            
    ans += len(str(num))
    print(ans)

else:
    print('0')