import sys
sys.setrecursionlimit(int(1e9))

def dfs(n, x, y, target):
    if not 0 <= x < n or not 0 <= y < n: #범위를 벗어나면 종료
        return

    elif target == 'R' or target == 'G': # 빨강이나 초록인데 블루면 종료
        if graph[x][y] != 'R' and graph[x][y] != 'G':
            return

    elif  target == 'B': # 파랑을 찾는데 레드나 그린이면 종료
        if graph[x][y] != 'B':
            return

    graph[x][y] = '0'
    dfs(n, x - 1, y, target)
    dfs(n, x, y - 1, target)
    dfs(n, x + 1, y, target)
    dfs(n, x, y + 1, target)

def dfs1(n, x, y, target):
    if not 0 <= x < n or not 0 <= y < n or graph1[x][y] != target:
        return

    graph1[x][y] = '0'
    dfs1(n, x - 1, y, target)
    dfs1(n, x, y - 1, target)
    dfs1(n, x + 1, y, target)
    dfs1(n, x, y + 1, target)




n = int(input())
graph = []
result = []
CB_person = 0
person = 0
for i in range(n):
    a = list(map(str, input()))
    graph.append(a)

graph1 = [i[:] for i in graph]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            dfs(n, i, j, 'R')
            CB_person += 1

        elif graph[i][j] == 'G':
            dfs(n, i, j, 'G')
            CB_person += 1

        elif graph[i][j] == 'B':
            dfs(n, i, j, 'B')
            CB_person += 1

for i in range(n):
    for j in range(n):
        if graph1[i][j] == 'R':
            dfs1(n, i, j, 'R')
            person += 1


        elif graph1[i][j] == 'G':
            dfs1(n, i, j, 'G')
            person += 1

        elif graph1[i][j] == 'B':
            dfs1(n, i, j, 'B')
            person += 1

print(person, end = ' ')
print(CB_person)