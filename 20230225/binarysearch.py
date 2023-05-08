from sys import stdin
input = stdin.readline
def BinarySearch(start, goal, end):
    while start<=end:
        mid = (start + end) // 2
        if goal == n_li[mid]:
            return mid
        elif goal < n_li[mid]:
            end = mid -1 
        else:
            start = mid + 1
    return None

n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

n_li.sort()

for i in m_li:
    r = BinarySearch(0, i, m-1)
    if r:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')