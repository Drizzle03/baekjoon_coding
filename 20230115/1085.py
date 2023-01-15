x, y, w, h = map(int, input().split())
ary = [x, w-x, y, h-y]
print(min(ary))