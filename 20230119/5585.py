n = int(input())
num = 1000-n #거슬러줄 잔돈의 수
cnt = 0
while(num>0):
    if(num >= 500):
        num-= 500
        cnt +=1
    elif(num >= 100):
        num -= 100
        cnt+=1
    elif(num >= 50):
        num -= 50
        cnt+=1

    elif(num >= 10):
        num -= 10
        cnt+=1

    elif(num >= 5):
        num -= 5
        cnt+=1

    else:
        num -= 1
        cnt+=1

print(cnt)