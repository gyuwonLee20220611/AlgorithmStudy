import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = [[]for i in range(n + 1)]

for i in range(m):
    a, node, dis = map(int, input().split())
    graph[a].append((node, dis))

distance = [INF] * (n + 1)

def dijkstra(start):
    distance[start] = 0
    que = []
    heapq.heappush(que, (start, 0))
    while que:
        now, dist =  heapq.heappop(que)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (i[0], cost))
dijkstra(c)

cnt = -1 # 시작노드가 cnt에 무조건 추가되기 때문에 -1로 시작
for i in range(n + 1):
    if distance[i] == INF:
        distance[i] = 0
    else:
        cnt += 1

print(cnt, max(distance))