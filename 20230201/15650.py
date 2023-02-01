N, M = map(int, input().split())
ans = []

def back():
    if len(ans) == M:
        p_ans = sorted(ans)
        print(" ".join(map(str, p_ans)))
        return

    for i in range(1,N+1):
        if len(ans) > 0:
            if not i in ans and ans[-1] < i:
                ans.append(i)
                back()
                ans.pop()

        elif not i in ans:
                ans.append(i)
                back()
                ans.pop()

back()