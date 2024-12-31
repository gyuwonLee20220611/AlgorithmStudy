import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
distance = []

for i in range(1, n + 1):
    graph[i][i] = 0
    graph[i][0] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[i][j] + graph[k][i])

result = 0
Min = INF
for i in range(1, n + 1):
    if sum(graph[i]) < Min:
        result = i
        Min = sum(graph[i])

print(result)