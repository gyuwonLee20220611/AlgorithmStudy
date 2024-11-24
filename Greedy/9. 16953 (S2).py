n,m = map(int, input().split())
cnt = 1

while n < m :
    if m % 2 == 0:
        m /= 2
        cnt += 1
    else:
        m = (m-1) / 10
        cnt += 1

if n == m:
    print(cnt)
else:
    print(-1)