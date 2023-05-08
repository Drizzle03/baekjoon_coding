from sys import stdin
input = stdin.readline
from itertools import product
t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 0

    for i in range(2,n+1):
        li = list(product([1,2,3], repeat=i))
        for j in li:
            if sum(j) == n:
                cnt +=1
    print(cnt)