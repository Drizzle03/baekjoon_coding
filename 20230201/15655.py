n, m = map(int, input().split())
n_li = list(map(int, input().split()))
ans = []
n_li.sort()

def back():
    for i in n_li:
        if len(ans) == m:
            print(" ".join(map(str, ans)))
            return

        if len(ans) == 0:
            ans.append(i)
            back()
            ans.pop()

        elif not i in ans and ans[-1] < i:
            ans.append(i)
            back()
            ans.pop()

back()