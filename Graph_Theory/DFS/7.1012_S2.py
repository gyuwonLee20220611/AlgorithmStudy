import sys
sys.setrecursionlimit(10**6)

def dfs(graph, x, y, n, m):
    if not 0 <= x < n or not 0 <= y < m or graph[x][y] == 0:
        return
    graph[x][y] = 0
    dfs(graph, x - 1, y, n, m)
    dfs(graph, x, y - 1, n, m)
    dfs(graph, x + 1, y, n, m)
    dfs(graph, x, y + 1, n, m)

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    graph = [[0 for i in range(m)]for i in range(n)]
    cabbage = []
    cnt = 0

    for i in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
        cabbage.append((x, y))

    for x, y in cabbage:
        if graph[x][y] == 1:
            dfs(graph, x, y, n, m)
            cnt += 1
    print(cnt)