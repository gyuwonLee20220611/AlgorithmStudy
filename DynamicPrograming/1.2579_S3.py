n = int(input())
step = [0]
for i in range(n):
    step.append(int(input()))



if n == 1:
    print(step[1])

elif n == 2:
    print(step[1] + step[2])


else:
    d = [0] * (n + 1)
    d[1] = step[1]
    d[2] = step[1] + step[2]
    for i in range(3, n + 1):
        d[i] = max(d[i - 2] + step[i], d[i - 3] + step[i] + step[i - 1])

    print(d[n])