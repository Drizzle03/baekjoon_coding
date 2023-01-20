n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

frist = data[n - 1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수
cnt = int(m/(k+1)) * k
# k+1로 나누어 떨어지지 않은 경우 == 큰 수로만 더해지다 끝났다.
cnt += m % (k+1)

r = 0

#큰 수의 횟수 * 큰 수
r += (cnt) * frist
# (숫자 더해지는 횟수 - 큰 수 횟수)는 즉 그 다음 큰 수가 더해진 수 이므로
r += (m - cnt) * second

print(r)