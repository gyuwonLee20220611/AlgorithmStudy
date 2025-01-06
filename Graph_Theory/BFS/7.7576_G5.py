from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, x, y, n, m):
    que = deque([(x, y)])
    move_x = [-1, 0, 1, 0]
    move_y = [0, -1, 0, 1]
    while que:
        x, y = que.popleft()

        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if not 0 <= dx < n or not 0 <= dy < m or graph[dx][dy] == -1 or graph[dx][dy] == 1:
                continue
            else:
                if graph[dx][dy] != 0 and graph[x][y] + 1 < graph[dx][dy]:
                    graph[dx][dy] = graph[x][y] + 1
                    que.append((dx, dy))

                elif graph[dx][dy] == 0:
                    graph[dx][dy] = graph[x][y] + 1
                    que.append((dx,dy))

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs(graph, i, j, n, m)
max_num = 0

for i in graph:
    if 0 in i:
        print(-1)
        break
    else:
        max_num = max(max_num, max(i))
else:
    print(max_num - 1)


