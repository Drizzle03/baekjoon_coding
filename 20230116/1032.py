from sys import stdin

n = int(input())
ary = [""]*n

for i in range(n): ary[i] = stdin.readline().strip()

answer_record = [0]*len(ary[0])
answer = ""

# 3번 확인 돌림
for i in range(1, n):
    # 글자수 만큼 또 비교해봐
    for j in range(len(ary[0])):
        # ary[0]번에 들어간 문자열이랑 2,3번째꺼랑 다르면 기록
        if(ary[0][j] != ary[i][j]):
            answer_record[j] += 1
        

for i in range(len(ary[0])):
    if(answer_record[i]>0):
        answer+="?"
    else:
        answer+=ary[0][i]

print(answer)
