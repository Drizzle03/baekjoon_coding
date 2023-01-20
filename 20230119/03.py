# 취업을 위한 코딩테스트 그리디 실전연습 3번 : 숫자 카드 게임 문제
from sys import stdin

n, m = map(int, input().split())
li = []

#입력
for i in range(n):
    li.append(list(map(int, stdin.readline().split())))

max = -1
for j in range(n):
    if(min(li[i]) > max):
        max = min(li[i])

print(max)