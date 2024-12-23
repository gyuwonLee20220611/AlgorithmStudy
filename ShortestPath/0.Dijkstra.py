INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[]for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node(num2):
    min_value = INF
    index = 0
    for j in range(1, num2 + 1):
        if distance[j] < min_value and not visited[j]:
            min_value = distance[j]
            index = j
    return index

def dijkstra(start, num):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n - 1):
        now = get_smallest_node(num)
        visited[now] = True
        for j in graph[now]:
            cost = j[1] + distance[now]
            if distance[j[0]] > cost:
                distance[j[0]] = cost



dijkstra(start, n)
print(distance)
