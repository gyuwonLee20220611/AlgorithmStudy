n, m = map(int, input().split())
cnt = 0
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, ):
    if x <= -1 or x >= n or y <= -1 or y >= m:
         return False
    else:
        if graph[x][y] == 0:
            graph[x][y] = 1

            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

            return True

        else:
            return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1
        else:
            continue
print(cnt)