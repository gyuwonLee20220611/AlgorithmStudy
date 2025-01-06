def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parents(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



v, e = map(int, input().split())
parents = [i for i in range(v + 1)]

for i in range(e):
    a, b = map(int, input().split())
    union_parents(parents, a, b)

print("각 원소가 속한 그룹: ", end = '')
for i in range(1, v + 1):
    print(find_parent(parents, i), end = ' ')

print()

print("부모 테이블: ", end = '')
for i in range(1, v + 1):
    print(parents[i], end = ' ')