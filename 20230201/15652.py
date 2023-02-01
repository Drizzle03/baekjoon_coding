n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str,ans)))
        return

    for i in range(1, n+1):
        if len(ans) > 0:
            if(i>=ans[-1]):
                ans.append(i)
                back()
                ans.pop()
        elif len(ans) == 0:
            ans.append(i)
            back()
            ans.pop()

back()