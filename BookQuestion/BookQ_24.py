n = int(input())
house = list(map(int, input().split()))
house.sort()

if len(house) % 2 == 0:
    print(house[len(house) // 2 - 1])
elif len(house) % 2 == 1:
    print(house[(len(house) // 2)])
