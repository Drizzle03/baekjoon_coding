T = int(input())
cnt_A = 0
cnt_B = 0
cnt_C = 0

A = 300
B = 60
C = 10

if(T >= A):
    cnt_A = T // A
    T %= A

if(T>=B):
    cnt_B = T // B
    T %= B

if(T>=C):
    cnt_C = T // C
    T %= C

if(T > 0):
    print(-1)
else:
    print(cnt_A, cnt_B, cnt_C)