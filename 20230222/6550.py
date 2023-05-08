# 입력값을 아예 안 주는 경우 전까지 실행하는 예외처리
while True:
    try:
        s, t = map(str, input().split())

        idx = 0
        for i in t:
            if i == s[idx]:
                idx+=1
                if idx == len(s):
                    print("Yes")
                    break
        else:
            print("No")
    except:
        break