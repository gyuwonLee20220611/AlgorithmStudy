n = int(input())
m = int(input())
ls = []
infected = [1]

for i in range(m):
    ls.append(list(map(int, input().split())))

def dfs(x):
    for i in range(m):
        if ls[i][0] == x and ls[i][1] not in infected:
            infected.append(ls[i][1])
            dfs(ls[i][1])

        elif ls[i][1] == x and ls[i][0] not in infected:
            infected.append(ls[i][0])
            dfs(ls[i][0])

    return 0

dfs(1)
print(len(infected)-1)