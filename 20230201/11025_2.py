from sys import stdin
n, k = map(int, stdin.readline().split())
last = 0

for i in range(1,n+1):
    last = (last+k-1)%i+1
print(last)