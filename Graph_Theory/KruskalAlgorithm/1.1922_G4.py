def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())
parents = [i for i in range(v + 1)]
result = 0

edges = []
for _ in range(e):
    a, b, dis = map(int, input().split())
    edges.append((dis, a, b))

edges.sort()

for i in edges:
    dist, node1, node2 = i
    if find_parent(parents, node1) != find_parent(parents, node2):
        union_parent(parents, node1, node2)
        result += dist

print(result)