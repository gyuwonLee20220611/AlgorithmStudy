t = int(input())
n = []
for i in range(t):
    n.append(int(input()))
s_n = sorted(n)

if s_n[-1] == 1:
    print(1)

elif s_n[-1] == 2:
    print(1)

elif s_n[-1] == 3:
    print(1)

else:
    p = [0] * (s_n[-1])
    p[0] = 1
    p[1] = 1
    p[2] = 1

    for i in range(3, s_n[-1]):
        p[i] = p[i - 2] + p[i - 3]

    for j in n:
        print(p[j - 1])
