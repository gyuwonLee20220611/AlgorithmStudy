#pypy로 성공.. 파이썬은 너무 느린걸까?
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph = [[INF] * (v + 1) for i in range(v + 1)]
result = INF

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, v + 1):
    for j in range(1, v + 1):
        for k in range(1, v + 1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            result = min(result, graph[j][i] + graph[i][j])

if result == INF:
    print(-1)
else:
    print(result)