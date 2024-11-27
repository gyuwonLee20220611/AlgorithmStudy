n = int(input())
ls = []
rank = 1
rank_ls =[1 for i in range(n)]

for i in range(n):
    ls.append(tuple(map(int,input().split())))

for j in ls:
    for k in range(n):
        if j[0] <= ls[k][0] and j[1] <= ls[k][1]:
            continue
        elif j[0] <= ls[k][0] or j[1] <= ls[k][1]:
            rank_ls[k] = rank
    rank += 1

print(rank_ls)