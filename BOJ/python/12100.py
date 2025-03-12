from copy import deepcopy


def mainf(board, step, move):
    global answer

    copy_board = deepcopy(board)

    if step == 5:  # the end
        max_val = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] > max_val:
                    max_val = board[i][j]
        if answer < max_val:
            answer = max_val

    elif move == "left":
        next_board = left(copy_board)
        mainf(next_board, step + 1, "left")
        mainf(next_board, step + 1, "right")
        mainf(next_board, step + 1, "up")
        mainf(next_board, step + 1, "down")
    elif move == "right":
        next_board = right(copy_board)
        mainf(next_board, step + 1, "right")
        mainf(next_board, step + 1, "left")
        mainf(next_board, step + 1, "up")
        mainf(next_board, step + 1, "down")
    elif move == "up":
        next_board = up(copy_board)
        mainf(next_board, step + 1, "up")
        mainf(next_board, step + 1, "right")
        mainf(next_board, step + 1, "left")
        mainf(next_board, step + 1, "down")
    else:  # move == "down"
        next_board = down(copy_board)
        mainf(next_board, step + 1, "right")
        mainf(next_board, step + 1, "down")
        mainf(next_board, step + 1, "up")
        mainf(next_board, step + 1, "left")


def right(bd):
    global n

    for i in range(n):
        cnt = n-1
        for j in range(1, n):
            if bd[i][n-j-1] != 0:
                if bd[i][cnt] == 0:
                    bd[i][cnt] = bd[i][n-j-1]
                    bd[i][n-j-1] = 0
                elif bd[i][n-j-1] == bd[i][cnt]:
                    bd[i][cnt] = bd[i][n-j-1] * 2
                    bd[i][n-j-1] = 0
                    cnt -= 1
                else:
                    cnt -= 1
                    bd[i][cnt] = bd[i][n-j-1]
                    if cnt != n-j-1:
                        bd[i][n-j-1] = 0

    return bd


def up(bd):
    global n

    for i in range(n):
        cnt = 0
        for j in range(1, n):
            if bd[j][i] != 0:
                if bd[cnt][i] == 0:
                    bd[cnt][i] = bd[j][i]
                    bd[j][i] = 0
                elif bd[j][i] == bd[cnt][i]:
                    bd[cnt][i] = bd[j][i] * 2
                    bd[j][i] = 0
                    cnt += 1
                else:
                    cnt += 1
                    bd[cnt][i] = bd[j][i]
                    if cnt != j:
                        bd[j][i] = 0

    return bd


def down(bd):
    global n

    for i in range(n):
        cnt = n-1
        for j in range(1, n):
            if bd[n-j-1][i] != 0:
                if bd[cnt][i] == 0:
                    bd[cnt][i] = bd[n-j-1][i]
                    bd[n-j-1][i] = 0
                elif bd[n-j-1][i] == bd[cnt][i]:
                    bd[cnt][i] = bd[n-j-1][i] * 2
                    bd[n-j-1][i] = 0
                    cnt -= 1
                else:
                    cnt -= 1
                    bd[cnt][i] = bd[n-j-1][i]
                    if cnt != n-j-1:
                        bd[n-j-1][i] = 0

    return bd


def left(bd):
    global n

    for i in range(n):
        cnt = 0
        for j in range(1, n):
            if bd[i][j] != 0:
                if bd[i][cnt] == 0:
                    bd[i][cnt] = bd[i][j]
                    bd[i][j] = 0
                elif bd[i][j] == bd[i][cnt]:
                    bd[i][cnt] = bd[i][j] * 2
                    bd[i][j] = 0
                    cnt += 1
                else:
                    cnt += 1
                    bd[i][cnt] = bd[i][j]
                    if cnt != j:
                        bd[i][j] = 0

    return bd


n = int(input())

if n == 1:
    print(int(input()))

else:
    answer = 0
    bmap = []
    for i in range(n):
        bmap.append(list(map(int, input().split())))

    mainf(bmap, 0, "left")
    mainf(bmap, 0, "right")
    mainf(bmap, 0, "up")
    mainf(bmap, 0, "down")

    print(answer)