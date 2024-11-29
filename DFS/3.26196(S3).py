board = []
for i in range(5):
    board.append(list(map(int, input().split())))
x, y = map(int, input().split())
ls = []
def dfs(x, y, apple, move):
    if x <= -1 or x >= 5 or y <= -1 or y >= 5 or board[x][y] == -1:
        return False

    elif apple < 2:
        move += 1
        if board[x][y] == 1:
            apple += 1
        if move < 3:
            dfs(x - 1, y, apple, move)
            dfs(x + 1, y, apple, move)
            dfs(x, y + 1, apple, move)
            dfs(x, y - 1, apple, move)
        else:
            return False
    else:
        ls.append(1)
        return True

dfs(x, y, 0, 0)

if 1 in ls:
    print(1)
else:
    print(0)



