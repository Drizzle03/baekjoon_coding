from itertools import permutations

n = int(input())
rng_li = list(range(1,n+1))
li = permutations(rng_li,n)

for i in li:
    print(*i)

