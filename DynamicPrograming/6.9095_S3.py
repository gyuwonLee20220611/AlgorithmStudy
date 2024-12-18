t = int(input())
n = []
for i in range(t):
    n.append(int(input()))

d = [0] * 12
d[1] = 1
d[2] = 2
d[3] = 4

for j in range(4, 12):
    d[j] = d[j - 3] + d[j - 2] + d[j - 1]

for i in n:
    print(d[i])