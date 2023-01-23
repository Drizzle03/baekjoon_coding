from sys import stdin
input = stdin.readline

from collections import deque

# 웹페이지 종류 수, 수행 작업 개수, 최대 캐시 용량
N, Q, C = map(int, input().split())
cash_size = list(map(int, input().split()))

total_cash = 0
nowpage = 0
front = deque()
back = deque()

# 작업 입력
for _ in range(Q):
    cmd = list(map(str, input().split()))

    # 뒤로 가기
    if cmd[0] == 'B':
        if(len(back) != 0):
            front.append(nowpage) #현재 보고 있던 웹페이지 앞으로 가기 공간 저장
            nowpage = back.pop() #뒤로 가기 공간 중 최근 페이지 접속, 및 기록 삭제

    # 앞으로 가기
    if cmd[0] == 'F':
        if(len(front) != 0):
            back.append(nowpage) #현재 보고 있던 웹페이지 뒤로 가기 공간 저장
            nowpage = front.pop() #앞으로 가기 공간 중 최근 페이지 접속, 및 기록 삭제

    # i번 웹페이지 접속
    if cmd[0] == 'A':
        # front에 있던 캐시 삭제
        if(nowpage != 0): #사이트에 처음 접속하지 않을 경우
            remove_cash = sum([cash_size[fc-1] for fc in front])
            total_cash -= remove_cash
            front.clear()
            
            back.append(nowpage) # 현재 페이지 뒤로 가기 공간 추가
        nowpage = int(cmd[1]) #다음 접속 페이지 > 현재 접속 페이지 갱신
        total_cash += cash_size[nowpage-1] #현재 페이지 캐시 용량 추가

        if(total_cash > C): #캐시 용량 초과 시
            remove_page = back.popleft() # 방문한지 제일 오래된 데이터 삭제
            total_cash -= cash_size[remove_page-1] #캐시 용량 삭제
            
    # 압축 실행
    if cmd[0] == 'C':
        for pagenum in range(1,N+1): #페이지 갯수만큼
            page_cnt = back.count(pagenum) #i번째 페이지의 갯수 카운팅
            if(page_cnt > 1): #같은 페이지 수가 2개 이상일 때
                for j in range(page_cnt-1): #1개를 남겨두고 삭제
                    total_cash -= cash_size[pagenum-1] #pagenum이 1부터니까, -1씩해서 사이즈 접근
                    back.remove(pagenum) #pagenu 값 삭제

print(nowpage)

back_log = list(back)[::-1]
front_log = list(front)[::-1]

if(len(back_log)==0): back_log = [-1]
if(len(front_log)==0): front_log = [-1]

print(*back_log)
print(*front_log)