ls = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(ls)):
    min_index = i
    for j in range(i, len(ls),):
        if ls[min_index] > ls[j]:
            min_index = j

    ls[i], ls[min_index] = ls[min_index], ls[i]

print(ls)
