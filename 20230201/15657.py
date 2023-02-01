n, m = map(int, input().split())
n_li = list(map(int, input().split()))
n_li.sort()
ans = []

def back():
    for i in n_li:
        if len(ans) == m:
            print(" ".join(map(str, ans)))
            return

        if len(ans) == 0:
            ans.append(i)
            back()
            ans.pop()

        elif ans[-1] <= i:
            ans.append(i)
            back()
            ans.pop()
back()