n = int(input())
money = list(map(int,input().split()))
money.sort()
target = 1

for i in money:
    if i > target:
        break
    else:
        target += i

print(target)