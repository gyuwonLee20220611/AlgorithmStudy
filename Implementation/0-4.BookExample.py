n, m = map(int, input().split())
men = list(map(int, input().split()))
px = men[0]
py = men[1]
drc = men[2]
Map = []
cnt = 1
turn = 0

for j in range(m):
        Map.append(list(map(int, input().split())))
Map[px][py] = 1

while True:
    if drc == 0:
        if Map[px][py-1] == 0:
            Map[px][py-1] = 1
            py -= 1
            cnt +=1
            turn = 0
        else:
            drc += 1
            turn +=1

    elif drc == 1:
        if Map[px-1][py] == 0:
            Map[px-1][py] = 1
            px -= 1
            cnt += 1
            turn = 0
        else:
            drc += 1
            turn += 1

    elif drc == 2:
        if Map[px][py+1] == 0:
            Map[px][py+1] = 1
            py += 1
            cnt += 1
            turn = 0
        else:
            drc += 1
            turn += 1

    elif drc == 3:
        if Map[px+1][py] == 0:
            Map[px+1][py] = 1
            px += 1
            cnt += 1
            turn = 0
        else:
            drc -= 3
            turn += 1

    if turn >= 4:
        break

print(cnt)