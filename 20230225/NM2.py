def dfs():
    if len(s) == m:
        print(' '.join(map(str, s))) #join은 문자열만 가능이니까 
    for i in range(1, n+1):
        if len(s) > 0:
            if (i in s) or (s[-1] > i):
                continue
        visited[i] = True
        s.append(i) #스택에 추가하고
        dfs() #dfs 호출해서 이후 값 추가
        s.pop()
        visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n+1)
s = []
dfs()
