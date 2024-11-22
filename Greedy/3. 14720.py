n = int(input())
cnt = 0
order = [0,1,2]
milk = list(map(int, input().split()))
result = 0


for i in range(n):
    if cnt == 3:
        cnt = 0
    if milk[i] == order[cnt]:
        result += 1
        cnt += 1

print(result)