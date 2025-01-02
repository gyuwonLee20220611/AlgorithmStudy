from collections import deque

n, m = map(int, input().split())
graph = []
dx = []
dy

for i in range(n):
    graph.append(list(map(int,input())))

def bfs():
    que = deque([0, 0])
    while que:
