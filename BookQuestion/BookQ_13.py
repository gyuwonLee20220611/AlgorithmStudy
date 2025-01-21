import sys
from itertools import combinations
input = sys.stdin.readline

def setting(array):
    return array[-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

house = []
chicken = []
distance = []

# 치킨집과 집의 좌표를 기록
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            house.append((x, y))
        if graph[x][y] == 2:
            chicken.append((x, y))

# 각 치킨집과 집사이의 거리를 구하고 distance에 저장
for x1, y1 in house:
    ls = []
    for x2, y2 in chicken:
        ls.append(abs(x1 - x2) + abs(y1 - y2))
    distance.append(ls)

array = [i for i in range(len(chicken))]
min_dis = int(1e9)
combi = combinations(array, m)
result = int(1e9)
cnt = 0
for i in combi:
    for j in range(len(house)):
        min_dis = int(1e9)
        for k in i:
            min_dis = min(min_dis, distance[j][k])

        cnt += min_dis

    result = min(result, cnt)
    cnt = 0

print(result)