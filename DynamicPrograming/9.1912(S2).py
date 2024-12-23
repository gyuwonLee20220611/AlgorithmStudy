n = int(input())
ls = [0] + list(map(int, input().split()))

d = [0] * 11

d[1] = ls[1]

for i in range(2, n + 1):
    if ls[i] >= 0:
        d[i] = max(d[i - 1], d[i - 1] + ls[i])
    else:
        d[i] = 0

print(d)