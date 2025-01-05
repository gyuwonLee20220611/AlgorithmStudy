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
visited= [False for i in range(9)]
def dfs(visited, v):
    visited[v] = True
    print(v,end = " ")
    for i in graph[v]:
        if not visited[i]:
            dfs(visited, i)

dfs(visited,1)
