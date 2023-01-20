number = "1231234"
k = 3

num = []
#리스트로 변환
for i in range(len(number)):
    num.append(number[i])
    
#정렬
num.sort()
newnum = num[:k]    

answer = ''
cnt = 0
record = [0]*len(number)
#제거 숫자를 다 달성한다면
while(k>0):
    for i in range(len(number)):
        #만약 앞에 있는 게 newnum 0번째 요소랑 같다면 제거
        if(k<=0): break
        if (number[i] == newnum[cnt] and record[i] == 0):
            k -=1
            record[i] = 1
            cnt+=1
            break

for i in range(len(number)):
    if(record[i] == 0):
        answer += number[i]
print(answer)

# for i in range(len(number)):
#     temp = list(set(newnum) - set(number[i])) #제거해야할 리스트에 해당 값이 있다면
#     print(i, "temp값 : ", temp)

#     if(len(temp) != len(newnum) and k>0): #만약 템프값에 변화가 있다면, 그 값이 존재한다는 것임.
#         k -=1
#         print("제거")
#     else:
#         answer += number[i]
#         print("추가")
