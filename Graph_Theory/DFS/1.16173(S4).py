n = int(input())
ls=[]
result =[]

for i in range(n):
    ls.append(list(map(int,input().split())))

def dfs(y,x):
    step = 0
    if "True" in result:
        return False
    elif x <= -1 or x >= n or y <= -1 or y >= n:
        result.append("False")
        return False
    elif ls[x][y] == -1:
        result.append("True")
        return True
    else:
        step = ls[x][y]
        if step == 0:
            return False
        dfs(y, x + step)
        dfs(y + step, x)

dfs(0, 0)
if "True" in result:
    print("HaruHaru")
else:
    print("Hing")