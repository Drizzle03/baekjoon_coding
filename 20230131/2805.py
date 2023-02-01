def bianrySearch(start, mid, target, end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        #잘린값 구하기
        tree_cut = [i-mid for i in tree if i>mid]
        if sum(tree_cut) < target:
            end = mid - 1
    
        elif sum(tree_cut) > target:
            start = mid + 1
            result = mid
        else: #sum == target일 때,
            result = mid
            return result
    return result

n, m = map(int, input().split())
tree = list(map(int, input().split()))
result = bianrySearch(min(tree), 0, m, max(tree))
print(result)
