n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))

for i in m_li:
    if i in n_li:
        print("yes", end = ' ')
    else:
        print("no", end=' ')