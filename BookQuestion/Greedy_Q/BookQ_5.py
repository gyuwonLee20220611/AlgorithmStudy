n, m  = map(int, input().split())
ball = list(map(int, input().split()))
cnt = 0

for i in range(len(ball)):
    for j in range(i, len(ball)):
        if ball[i] == ball[j]:
            continue
        else:
            cnt += 1
print(cnt)