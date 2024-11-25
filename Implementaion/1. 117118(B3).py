n = int(input())
people = []

for i in range(n):
    people.append(tuple(map(int, input().split())))
print(max(people))

for i in people:
    