n = int(input())
graph = []
ans = 0
estate = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, graph, estate, n):
    if not 0 <= x < n or not 0 <= y < n or graph[x][y] != 1:
        return
    graph[x][y] = 0
    estate[-1] += 1

    dfs(x - 1, y, graph, estate, n)
    dfs(x, y - 1, graph, estate, n)
    dfs(x + 1, y, graph, estate, n)
    dfs(x, y + 1, graph, estate, n)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            estate.append(0)
            dfs(i, j, graph, estate, n)
            ans += 1

print(ans)
estate.sort()
for i in estate:
    print(i)
