import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v + 1)]
for i in range(e):
    a, node, dis = map(int, input().split())
    graph[a].append((node, dis))
distance = [INF] * (v + 1)


def dijkstra(start):
    distance[start] = 0
    que = []
    heapq.heappush(que, (0 ,start))

    while que:
        dist, now = heapq.heappop(que)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

dijkstra(k)
for i in distance[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)