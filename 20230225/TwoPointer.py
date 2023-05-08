n = 5
m = 5
data = [1,2,3,2,5]
cnt = 0
start, end = 0, 0
sum_value = 0

# 부분합 >= 목표값 -> start +=1
# 부분합 == 목표값 -> cnt += 1
# 부분합 < 목표값 -> end += 1

for start in range(n):
    while sum_value < m and end < n:
        sum_value += data[end]
        end += 1
    if sum_value == m:
        cnt += 1
    sum_value -= data[start]
