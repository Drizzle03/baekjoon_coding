n = 5
data = [10, 20, 30, 40, 50]

prefix = [0]*(n+1) #구간합

sum = 0
prefix[0] = 0
for i in range(0,n):
    sum += data[i]
    prefix[i+1] = sum

print(prefix)

left = 3
right = 4
print(prefix[right]-prefix[left-1])