import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for i in range(m + 2)]
for i in range(m):
    n_node, e_node, dis = map(int, input().split())
    graph[n_node].append((e_node, dis))
start, end = map(int, input().split())
distance = [INF] * (n + 1)

def dijkstra(start):
    distance[start] = 0
    que = []
    heapq.heappush(que, (start, 0))

    while que:
        now, dist = heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(que, (i[0], cost))

dijkstra(start)

print(distance[end])