# 보류 못 품
n, m = map(int, input().split())
n_li = list(map(int, input().split()))
n_li.sort()

ans = []
now = 0
now_index = -1

def back():
    global now
    global now_index

    for i in range(len(n_li)):
        if n_li[i] != now and i != now_index:
            if len(ans) == m:
                print(" ".join(map(str, ans)))
                return
            ans.append(n_li[i])
            back()
            now = ans.pop()
            now_index = i
back()
