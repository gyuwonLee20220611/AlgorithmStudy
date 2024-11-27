n = input()
x = ord(n[0])-96
y = int(n[1])
movement = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
cnt =0

for i in movement:
    dx = i[0] + x
    dy = i[1] + y
    if  dx <= 8 and dx >= 1 and dy <= 8 and dy >= 1:
        cnt += 1
    else:
        continue
print(cnt)