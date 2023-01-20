# 취업을 위한 코딩테스트 그리디 실전연습 2번 : 큰 수의 법칙 문제
# n개의 수열, m번 더하여, k 최대값
n, m, k = map(int, input().split())
ni = list(map(int, input().split()))

ni.sort(reverse=True)

cnt_m = 0
cnt_k = 0
i = 0
r = 0

while True:
    if(cnt_m >= m or i >= (n-1)):
        break
    elif(cnt_k >= k):
        cnt_m +=1
        r += ni[i+1]
        cnt_k = 0
    else:
        r += ni[i]
        cnt_m +=1
        cnt_k +=1 # 연속 더함 횟수 추가

print(r)