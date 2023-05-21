# a=input()
# a=a.upper()
# d={}
# for chr in a:
#     if chr in d:
#         d[chr]+=1
#     else:
#         d[chr]=1


li = {'a': 1, 
      'b': 32,
      'c': 3,
      'd': 4,
      'e' : 4}

max = -99
max_re = ''

for i in li:
    if li[i] > max:
        max_re = i
        max = li[i]

print(max, max_re)
