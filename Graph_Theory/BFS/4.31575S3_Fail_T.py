from collections import deque
n, m = map(int, input().split())
graph = []

for i in range(m):
    graph.append(list(map(int, input().split())))

def bfs(n, m):
    queue = deque([(0, 0)])
    move_x = [1, 0, -1 ,0]
    move_y = [0, 1, 0, -1]


    while queue:
        point = queue.popleft()
        x = point[0]
        y = point[1]
        graph[x][y] = 0

        for i in range(4):
            dx = move_x[i] + x
            dy = move_y[i] + y

            if not 0 <= dx < m or not 0 <= dy < n:
                continue

            if graph[dx][dy] == 0:
                continue

            else:
                queue.append((dx, dy))

                if dx == m - 1 and dy == n - 1:
                    return True

    return False

if bfs(n, m):
    print("Yes")
else:
    print("No")