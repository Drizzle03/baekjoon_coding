from sys import stdin

n = int(input())

li = []

#입력
for _ in range(n):
    s, e = map(int, input().split())
    li.append([s,e])

#끝 시간 기준 정렬
li[0] = sorted(li[0], reverse=True)
li = sorted(li, key=lambda x:(x[1]))

# 맨 뒷 팬 시작시간 - 맨 앞 팬 종료 시간
if li[-1][0] <= li[0][1]:
    print(0)
else:
    print(li[-1][0] - li[0][1])