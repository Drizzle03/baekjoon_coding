from sys import stdin
input = stdin.readline
s = input()
s = s[:-1]
n = int(input())

str_li =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
pt = False
for _ in range(n):
    t = input() #입력
    t = t[:-1]
    if not pt:
        t_li = [ord(j)-97 for j in t]
        for i in range(27):
            li =[str_li[(k+i)%26] for k in t_li]
            change = "".join(li)
            if s.startswith(change):
                opt = [str_li[((ord(m)-97)+(26-i))%26] for m in s]
                print("".join(opt))
                pt = True
                break