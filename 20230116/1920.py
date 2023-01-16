from sys import stdin

#ary 0 4 7
def binary_search(ary, start, end, target):
    mid = (start + end) // 2
    #mid = 3 + 4 //2 = 3
    # print("start : ", start,"end : ",end ,"mid : ", mid)

    if(start>end):
        return 0
    
    elif(ary[mid] == target):
        return 1

    elif(ary[mid]>target): #mid가 target 오른쪽에 있을 때,
        end = mid - 1

    elif(ary[mid]<target):
        start = mid +1

    return binary_search(ary, start, end, target)

N = int(input())
ary = list(map(int,input().split()))
ary.sort()

M = int(input())
m_li = list(map(int, input().split()))

for i in range(M):
    print(binary_search(ary, 0, N-1, m_li[i]))


