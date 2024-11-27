n = int(input())
ls = list(map(str, input().split()))
point = [1,1]

for i in ls:
    if i =='R' and point[1] < n:
        point[1] += 1
    elif i =='L' and point[1] > 1:
        point[1] -= 1
    elif i =='U' and point[0] > 1:
        point[0] -= 1
    elif i =='D' and point[0] < n:
        point[0] += 1

for j in point:
    print(j,end = " ")
