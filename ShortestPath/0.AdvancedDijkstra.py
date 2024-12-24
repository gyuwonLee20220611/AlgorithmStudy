import heapq
from pickle import GLOBAL

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, dis, node = map(int, input().split())
    graph[a].append((dis, node))

def advanced_dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    print(graph)


    while q:
        print(q)
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


advanced_dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
