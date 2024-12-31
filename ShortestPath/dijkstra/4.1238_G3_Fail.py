import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
distance = [[INF, INF]] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, node, dis = map(int, input().split())
    graph[a].append((node,dis))


def dijkstra(target):
    distance[target][0] = 1
    distance[target][1] = 2

    que = []
    heapq.heappush(que, (target, 0))

    while que:
        now, dist = heapq.heappop(que)
        if distance[now][0] < dist:
            continue

        for i in graph[now]:
            if now == target:
                cost = distance[now][1] + i[1]
                if distance[i[0]][1] > cost:
                    distance[i[0]][1] = cost
                    heapq.heappush(que, (now, cost))
            else:
                cost = distance[now][0] + i[1]
                if distance[i[0]][0] > cost:
                    distance[i[0]][0] = cost
                    heapq.heappush(que, (now, cost))
                if distance[i[0]][0] < distance[i[0]][1]:
                    distance[i[0]][1] = distance[i[0]][0]

dijkstra(x)
print(distance)