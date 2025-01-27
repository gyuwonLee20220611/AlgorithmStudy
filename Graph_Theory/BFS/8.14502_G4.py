from itertools import combinations, permutations
from collections import deque

def bfs(n, m):
    que = deque([])
    move_x = [-1, 0, 1, 0]
    move_y = [0, -1, 0, 1]
    for i in virus:
        que.append(i)
    cnt = len(virus)

    while que:
        x, y = que.popleft()
        for i in range(4):
            dx = move_x[i] + x
            dy = move_y[i] + y
            if not 0 <= dx < n or not 0 <= dy < m or copy_graph[dx][dy] == 1:
                continue
            elif copy_graph[dx][dy] == 0:
                copy_graph[dx][dy] = 2
                que.append((dx, dy))
                cnt += 1
    result.append(cnt)

n, m = map(int, input().split())
graph = []

blank = []
virus = []
result = []
cnt = 0

for i in range(n):
    graph.append(list(map(int, input().split())))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i, j))
        elif graph[i][j] == 1:
            cnt  += 1
        elif graph[i][j] == 2:
            virus.append((i, j))

combi_blank = list(combinations(blank, 3))

for i in combi_blank:
    copy_graph = [i[:]for i in graph]
    barrier1, barrier2, barrier3 = i
    copy_graph[barrier1[0]][barrier1[1]] = 1
    copy_graph[barrier2[0]][barrier2[1]] = 1
    copy_graph[barrier3[0]][barrier3[1]] = 1
    bfs(n, m)

print(n * m - (min(result) + cnt + 3))
