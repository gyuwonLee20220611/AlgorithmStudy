import sys
input = sys.stdin.readline

def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]

def union_parent(node1, node2):
    a = find_parent(node1)
    b = find_parent(node2)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))
    union_parent(u, v)

edges.sort()

for i in edges:
    node1, node2 = i
    if parent[node1] != parent[node2]:
        union_parent(node1, node2)

parent.sort()
cnt = 0
first = parent[0]
for i in parent:
    if i != first:
        first = i
        cnt += 1

print(cnt)