

def dfs():
    if len(s) == m: #현재 리스트의 길이가 m과 동일하다면 출력
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n+1): #동일하지 않다면 1의 숫자부터 n까지 for문
        if visited[i]: #이미 중복된 수열이 있다면 넘어감
            continue
        visited[i] = True #이미 중복된 수열이 없다면 방문 처리하고
        s.append(i) #값 삽입
        dfs() #dfs 호출
        s.pop() #dfs에서 빠져 나오면 값 하나를 제거함
        visited[i] = False #그리고 제거한 값을 다시 비방문 처리함

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()