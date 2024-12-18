n = int(input())
a_ls = list(map(int, input().split()))

d = [0] * 1001
d[1] = 1
if a_ls[0] < a_ls[1]:
    d[2] = 2
else:
    d[2] = 1

