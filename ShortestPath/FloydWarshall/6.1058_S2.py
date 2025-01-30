INF =int(1e9)

n = int(input())
graph = []
result = [0] * n

for i in range(n):
    graph.append(list(map(str, input())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'N':
            graph[i][j] = INF
        else:
            graph[i][j] = 1

for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(n):
    cnt = 0
    for j in range(n):
        if graph[i][j] < 3:
            if i == j:
                continue
            else:
                cnt += 1
    result.append(cnt)
print(max(result))