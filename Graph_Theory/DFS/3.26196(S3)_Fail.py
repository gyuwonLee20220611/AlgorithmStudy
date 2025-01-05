board = []
for i in range(5):
    board.append(list(map(int, input().split())))
r, c = map(int, input().split())
ls = []

def dfs(x, y, move, apple, graph):
    if not 0 <= x < 5 or not 0 <= y < 5:
        return True
    if board[x][y] == -1 or move > 3:
        return False


    if board[x][y] == 1:
        apple += 1
        if apple >= 2:
            ls.append(1)

dfs(r, c, 0, 0, board)
if 1 in ls:
    print(1)
else:
    print(0)