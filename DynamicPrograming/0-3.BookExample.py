n = int(input())
d = [0] * (n + 1)
d[0] = 1
d[1] = 3

if n == 1:
    print(d[0])

elif n == 2:
    print(d[1])

else:
    for i in range(2, n + 1):
        d[i] = d[i - 1] + (d[i - 2] * 2) % 769769

    print(d[n - 1])