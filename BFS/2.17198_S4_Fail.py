from collections import deque
graph = []

for i in range(10):
    graph.append(list(map(str, input())))

def bfs(x, y):
    queue = deque([(x, y)])
    move_x = [1, 0, -1, 0]
    move_y = [0, 1, 0, -1]
    cnt = 1

    while queue:
        point = queue.popleft()
        x = point[0]
        y = point[1]

        for i in range(4):

            dx = move_x[i] + x
            dy = move_y[i] + y

            if not 0<= dx < 10 or not 0 <= dy < 10:
                continue

            if graph[dy][dy] == 'R':
                continue

            if graph[dy][dx] =='B':
                continue

            if cnt == 1:
                graph[dy][dx] = cnt
                queue.append((dx, dy))

            elif graph[dy][dx] == '.':
                graph[dy][dx] = graph[y][x] + 1




bfs(3,2)

print(graph)