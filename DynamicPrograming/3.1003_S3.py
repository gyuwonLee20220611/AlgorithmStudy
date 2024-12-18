n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
a = max(ls)

d = [0] * (a + 2)
d[0] = (1, 0)
d[1] = (0, 1)

for i in range(2, a + 1):
    d[i] = (d[i - 1][0] + d[i - 2][0], d[i - 1][1] + d[i - 2][1])

for j in ls:
    print(d[j][0],d[j][1])