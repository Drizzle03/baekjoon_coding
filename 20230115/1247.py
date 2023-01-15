from sys import stdin
#sys 모듈 중 stdin만 임포트
for _ in range(3):
    N = int(stdin.readline())
    li = [int(stdin.readline()) for i in range(N)]
    if sum(li) == 0:
        print("0")
    elif sum(li) > 0:
        print("+")
    else:
        print("-")