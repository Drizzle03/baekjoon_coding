from sys import stdin
T = int(input())

N = []
#N 입력
for i in range(T):
    N.append(int(stdin.readline()))
    score = []
    index = 0
    cnt = 0

    #지원자 정보 입력
    for j in range(N[i]):
        a,b = map(int, stdin.readline().split())
        score.append([a,b])

    score = sorted(score, key=lambda score : (score[0],score[1]))
    
    # 스코어 n번째들 다 훑음
    for k in range(score[i]):
        
        if(score[k][0] == 1 or score[k][1] == 1):
            cnt += 1
        #우선순위 1이 없다면
        else:
            pass