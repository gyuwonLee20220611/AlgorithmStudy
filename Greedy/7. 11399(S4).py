n = int(input())
ls = list(map(int, input().split()))
ans = 0
cnt = 1
ls.sort()

for i in ls:
    time = 0
    for j in range(cnt):
        time += ls[j]
    cnt += 1
    ans += time

print(ans)