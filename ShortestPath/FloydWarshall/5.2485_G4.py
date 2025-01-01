import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] < INF or graph[j][i] < INF:
            continue
        else:
            break
    else:
        ans += 1

print(ans)