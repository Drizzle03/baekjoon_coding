#큰 수의 법칙

from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
li = list(map(int, input().split()))

li.sort(reverse=True)

s = 0
cnt = 0
for i in range(m):
    if cnt>=k:
        s += li[1]
        cnt = 0
    else:
        s += li[0]
        cnt += 1


print(s)
