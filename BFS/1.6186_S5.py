from collections import deque

def bfs(graph, x, y, Max_x, Max_y):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, -1, 0]
    queue = deque([(x,y)])

    while queue:
        point = queue.popleft()
        x = point[0]
        y = point[1]
        for i in range(4):
            dx = x + x_move[i]
            dy = y + y_move[i]

            if not 0 <= dx < Max_x or not 0 <= dy < Max_y:
                continue

            if graph[dx][dy] == '.':
                continue

            else:
                graph[dx][dy] = '.'

            queue.append((dx,dy))




n, m = map(int, input().split())
graph = []
cnt = 0

for i in range(n):
    graph.append(list(map(str, input())))

for i in range(n):
    for j in range(m):
         if graph[i][j] == '#':
             bfs(graph, i, j, n, m)
             cnt += 1

print(cnt)