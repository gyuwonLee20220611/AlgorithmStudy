n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))
money.sort(reverse = True)

d = [10001] * 10001
d[0] = 0
for i in range(1, m + 1):
    for j in money:
        if i - j < 0:
            d[i] = 10001

        elif i - j == 0:
            d[i] = 1

        else:
            d[i] = min(d[i], d[i - j] + 1)

if d[m] <= 10000:
    print(d[m])
else:
    print(-1)