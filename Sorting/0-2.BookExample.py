n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

def out_achievement(a):
    return a[1]

array.sort(key=lambda array: array[1])

for i in array:
    print(i[0], end = ' ')