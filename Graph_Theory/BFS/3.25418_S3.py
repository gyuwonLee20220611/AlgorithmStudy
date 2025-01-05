n, m = map(int, input().split())

cnt = 0

while n != m:

    if m / 2 < n:
        m -= 1
        cnt += 1

    elif m / 2 >= n:

        if m % 2 == 1:
            m -= 1
            cnt += 1

        else:
            m /= 2
            cnt += 1

print(cnt)