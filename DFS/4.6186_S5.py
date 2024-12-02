def dfs(x, y, n , m):

    if not 0 <= x < n or not 0 <= y < m:
        return False

    elif graph[x][y] == '#':
        graph[x][y] = '.'

        dfs(x - 1, y, n, m)
        dfs(x, y - 1, n, m)
        dfs(x + 1, y, n, m)
        dfs(x, y + 1, n ,m)
        return True

    else:
        return False




n, m = map(int, input().split())
graph = []
cnt = 0

for i in range(n):
    graph.append(list(map(str, input())))

for i in range(n):
    for j in range(m):
        if dfs(i, j, n ,m):
            cnt += 1


print(cnt)

