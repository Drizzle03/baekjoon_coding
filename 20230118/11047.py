#그리디 알고리즘 문제
from sys import stdin
N, K = map(int, stdin.readline().split())
A = []
cnt = 0

for _ in range(N):
    A.append(int(stdin.readline()))

for i in range(N-1, -1 , -1):
    temp = K // A[i]
    cnt += temp
    K -= temp*A[i]

print(cnt)