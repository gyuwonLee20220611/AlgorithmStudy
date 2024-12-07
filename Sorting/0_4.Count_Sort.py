array = [9, 1, 5, 6, 3, 3, 2, 7, 9, 5, 0]
biggest = max(array)
ls = [0 for i in range(biggest + 1)]

for i in array:
    ls[i] += 1


for j in range(len(ls)):
    for k in range(ls[j]):
        print(j,end = " ")