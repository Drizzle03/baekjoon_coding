array = [7,5,9,0,3,1,6,2,4,8]

#정렬 후 기존 리스트에 삽입
# array.sort()

#정렬 후 새로운 리스트 생성 후 대입
# 1. 그냥 전체 정렬
li = sorted(array)
print(li)

# 2. 부분 정렬
li = sorted(array[:5])
print(li)

# 3. 특정 키를 기준으로 정렬
array = [
    [1, 4],
    [5, 5],
    [0, 6],
    [5, 7],
    [3, 5],
    [6, 8],
    [6, 7]
]

# 0번 인덱스 기준 정렬
li = sorted(array)
print(li)

# 1번 인덱스 기준 정렬
li = sorted(array, key =lambda array:array[1])
print(li)

# 1번 인덱스 기준 정렬, and 1번 인덱스 값이 같다면, 같은 값들 중 0번 인덱스를 기준으로 정렬
li = sorted(array, key =lambda array:(array[1],array[0]))
print(li)

# 삽입 + 병합 정렬 > 하이브리드
# 최악 O(NlogN)


# 데이터 범위가 한정, 빠르게 동작해야해 > 계수 정렬

# print(array)
