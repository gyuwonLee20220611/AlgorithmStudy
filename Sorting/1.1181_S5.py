n = int(input())
array = []

for i in range(n):
    a = input()
    if (a, len(a)) in array:
        continue
    else:
        array.append((a, len(a)))

result = sorted(array, key = lambda x: [x[1], x[0]])

for i in result:
    print(i[0])
