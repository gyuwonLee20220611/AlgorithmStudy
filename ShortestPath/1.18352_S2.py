import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dijkstra(start):
    que = []
    heapq.heappush(que,(0, start))
    distance[start] = 0
    while que:
        dis, now = heapq.heappop(que)

        if dis > distance[now]:
            continue

        for i in graph[now]:
            if dis + 1 < distance[i]:
                distance[i] = dis + 1
                heapq.heappush(que,(dis + 1, i))


dijkstra(x)
if k in distance:
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
else:
    print(-1)
