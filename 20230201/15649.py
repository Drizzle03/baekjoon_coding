N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    
    for i in range(N+1):
        if not i in ans:
            ans.append(i)
            back()
            ans.pop()

back()