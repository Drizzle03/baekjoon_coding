# 취업을 위한 코딩테스트 그리디 실전연습 4번 : 1이 될 떄까지 문제

n, k = map(int, input().split())

cnt = 0
while(n > 1):
    if(n%k == 0):
        n/=k
        cnt+=1
    else:
        n-=1
        cnt+=1

print(cnt)