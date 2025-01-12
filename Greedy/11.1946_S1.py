import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    ls = []
    for j in range(n):
        a, b = map(int, input().split())
        ls.append((a, b))

    ls.sort()
    standard = ls[0][1]
    cnt = 1
    for j in range(1, n):
        if standard > ls[j][1]:
            cnt += 1
            standard = ls[j][1]

    print(cnt)