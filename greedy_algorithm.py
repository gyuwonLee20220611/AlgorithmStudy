n,m,k = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
result = 0

first = ls[-1]
second = ls[-2]

result += first * (m // k) * k
result += second * (m % k)

print(result)