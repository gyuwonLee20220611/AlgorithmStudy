from collections import deque

n, m, v = map(int, input().split())
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

def dfs(visited, graph ,start):
    print(start, end = ' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(visited, graph, i)
    return

def bfs(visited, graph, start):
    que = deque([start])
    visited[start] = True
    while que:
        q = que.popleft()
        print(q, end=' ')

        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                que.append(i)



dfs(visited_dfs, graph, v)
print()
bfs(visited_bfs, graph, v)