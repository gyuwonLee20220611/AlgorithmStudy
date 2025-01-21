n = int(input())
people = []
for i in range(n):
    a = list(map(str, input().split()))
    name = a[0]
    korean = int(a[1])
    english = int(a[2])
    math = int(a[3])
    people.append([korean, english, math, name])

answer = sorted(people, key = lambda x: (-x[0], x[1], -x[2], x[3]))

for i in answer:
    print(i[3])