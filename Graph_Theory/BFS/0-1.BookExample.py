from collections import deque

def bfs(graph, n, m):
    queue = deque([(0,0)])
    move_x = [1, 0, -1, 0]
    move_y = [0, 1, 0, -1]

    while queue:
        point = queue.popleft()
        x = point[0]
        y = point[1]

        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]

            if not 0 <= dx < n or not 0 <= dy < m:
                continue

            if graph[dx][dy] == 0:
                continue

            if graph[dx][dy] == 1:
                queue.append((dx, dy))
                graph[dx][dy] = graph[x][y] + 1
                if dx == n - 1 and dy == m - 1:
                    print(graph[dx][dy])
                    return 0


n, m = map(int,input().split())
graph = []

for i in range(n):
    graph.append (list(map(int, input())))

bfs(graph, n, m)