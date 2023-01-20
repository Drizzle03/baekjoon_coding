from sys import stdin
n = int(input())

student = []*n
#반 횟수 카운팅
s_cnt = [0]*n

for i in range(n):
    student.append(list(map(int, stdin.readline().split())))

for j in range(n):
    stu_ary=[0]*n
    for k in range(5): #j가 학생 번호고, k가 학년
        for l in range(n):
            if(j != l and student[j][k] == student[l][k] and stu_ary[l] == 0):
                s_cnt[j]+=1
                stu_ary[l] = 1

print(s_cnt)
print(s_cnt.index(max(s_cnt))+1)