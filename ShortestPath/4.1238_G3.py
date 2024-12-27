import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, node, dis = map(int, input().split())
    graph[a].append((node,dis))

def dijkstra(target):
    distance[target] = 0
    que = []
    heapq.heappush(que, (target, 0))

    while que:
        now, dist = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(que, (now, cost))

dijkstra(x)
print(distance)