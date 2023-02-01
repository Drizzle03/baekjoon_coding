n,m = map(int,input().split())
arr = list(map(int, input().split()))
 
left = 0
right = max(arr)
result = 0
while left <= right:
    mid = (left + right)//2
    total = 0
    for x in arr:
        if x > mid:
            total += x - mid

            
    if total == m:
        result = mid
        break
    if total < m:
        right = mid-1
    else:
        result = mid
        left = mid+1
print(result)