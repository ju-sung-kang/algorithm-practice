def findWord(r, c, word, step):
    global board
    global visited
    global longest
    global wordcnt
    global score

    dr = [0, 0, -1, 1, -1, -1, 1, 1]
    dc = [-1, 1, 0, 0, -1, 1, -1, 1]

    visited[r][c] = True

    if len(word) == step and finded[word] == 0:
        if len(longest) < len(word):
            longest = word
        elif len(longest) == len(word):
            tmp = ["", ""]
            tmp[0] = longest
            tmp[1] = word
            tmp.sort()
            longest = tmp[0]

        wordcnt += 1
        score += wordScore(word)
        finded[word] = 1

    elif step < len(word):
        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if (0<=nr<=3) and (0<=nc<=3) and (not visited[nr][nc]) and (w[step] == board[nr][nc]):
                findWord(nr, nc, word, step+1)

    visited[r][c] = False


def wordScore(word):
    length = len(word)
    if length <= 2:
        return 0
    elif length <= 4:
        return 1
    elif length == 5:
        return 2
    elif length == 6:
        return 3
    elif length == 7:
        return 5
    elif length == 8:
        return 11


w = int(input())
words = []
for i in range(w):
    words.append(input())


input()
board = []
visited = [[False]*4 for i in range(4)]
b = int(input())
for i in range(b):
    finded = {}
    for w in words:
        finded[w] = 0

    score = 0
    wordcnt = 0
    longest = ""
    board = []
    for j in range(4):  # 판을 저장
        board.append(list(input()))

    if i != b-1:
        input()

    for row in range(4):  # 단어 찾기
        for col in range(4):
            for w in words:
                if board[row][col] == w[0] and finded[w] == 0:
                    findWord(row, col, w, 1)

    print("%d %s %d" % (score, longest, wordcnt))