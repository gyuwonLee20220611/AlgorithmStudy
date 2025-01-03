from collections import deque

n, m = map(int, input().split())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    graph.append(list(map(int,input())))

def bfs():
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        for i in range(4):
            x1 = dx[i] + x
            y1 = dy[i] + y
            if 0 <= x1 < n and 0 <= y1 < m and graph[x1][y1] == 1:
                que.append((x1, y1))
                graph[x1][y1] = graph[x][y] + 1


bfs()
print(graph[n - 1][m - 1])