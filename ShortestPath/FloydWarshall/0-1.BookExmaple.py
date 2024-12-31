import sys
INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

end, stopover = map(int, input().split())


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
        if graph[i][j] == 1:
            graph[j][i] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            graph[j][k] = min(graph[j][k], graph[i][j] + graph[k][i])

if not graph[1][stopover] + graph[stopover][end] >= INF:
    print(graph[1][stopover] + graph[stopover][end])
else:
    print(-1)