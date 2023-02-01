from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])
maker = k-1
size = n

for _ in range(n-1):
    queue.remove(queue[maker])
    size -= 1
    if size != 0:
        maker = (maker+k-1)%size

print(queue[0])