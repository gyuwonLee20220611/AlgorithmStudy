from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


visited = [False for i in range(9)]
graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
             ]
bfs(graph, 1, visited)