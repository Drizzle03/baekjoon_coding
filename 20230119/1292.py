a,b = map(int, input().split())

ary = []
for i in range(1, b+1):
    ary += [i]*i

# print(ary)
print(sum(ary[a-1:b]))