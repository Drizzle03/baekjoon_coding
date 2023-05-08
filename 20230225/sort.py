n = int(input())
li = []

for _ in range(n):
    a,b = map(str, input().split())
    li.append((a,int(b)))

li = sorted(li, key = lambda x : x[1])

for i in range(n):
    print(li[i][0], end = ' ')