sig = input()

sign = []
num = []
temp = ''

for i in sig:
    #숫자일 때
    if((ord(i) >= 48) and (ord(i)) <= 57):
        temp = temp + i  
    else:
        sign.append(i)
        num.append(int(temp))
        temp = ''
    
num.append(int(temp))
sign.append('-1')
result = 0
minus_temp = 0

print(num)
print(sign)
# for i in range(len(num)-1):
#     if(sign[i]=='-'):
#         if(sign[i+1] == '\0' or sign[i+1] == 1): #식의 끝이거나, +면
#             minus_temp += num[i+1] #현재 값과 다음 