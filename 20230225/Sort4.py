n, k = map(int, input().split())
a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

temp = 0
a_li.sort()
b_li.sort(reverse=True)

for i in range(k):
    if a_li[i] >= b_li[i]:
        break
    if a_li[i] < b_li[i]:
        a_li[i], b_li[i] = b_li[i], a_li[i]
        
print(sum(a_li))