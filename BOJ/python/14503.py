import sys
sys.setrecursionlimit(10**6)                       # 재귀호출이 많이 필요해서 최대 재귀호출 제한을 늘림


def clean(turn):                                   # 로봇청소기의 작동을 정의
    global r, c, d                                   # r,c는 현재 행과 열 d는 현재 바라보는 방향
    global _map
    global cleaned                                   # 청소한 칸의 수 저장

    if _map[r][c] == 0:                              # 청소하지 않은 칸이라면 청소
        _map[r][c] = 2
        cleaned += 1

    nd = turn_left(d)                                # nd에 왼쪽 방향을 저장
    npos = go(r,c,nd)                                # npos에 왼쪽 좌표 저장
    if _map[npos[0]][npos[1]] == 0:                  # 왼쪽 청소를 안했다면 이동해서 청소함
        r, c = npos[0], npos[1]                        # 좌표 업데이트
        d = nd                                         # 방향 업데이트
        clean(0)                                       # 이동한 자리에서 청소하고 다시 후속 동작 반복
    else:                                            # 이미 청소되어있다면
        if turn <= 3:                                  # 네방향 다 탐색하지 않았다면 돌면서 계속 탐색
            d = nd
            clean(turn + 1)

    bpos = back(r,c,d)                             # 네방향 다 청소했거나 벽일경우 후진해야함
    if _map[bpos[0]][bpos[1]] != 1:                  # 후진할수 있다면
        r, c = bpos[0], bpos[1]                      # 후진
        clean(0)


def turn_left(dir):                                # 왼쪽 방향 return
    next_dir = (dir + 3) % 4
    return next_dir


def go(row, col, dir):                             # 방향별 직진한 뒤의 좌표 return
    if dir == 0:
        return row - 1, col
    elif dir == 1:
        return row, col + 1
    elif dir == 2:
        return row + 1, col
    else:  # dir == 3
        return row, col - 1


def back(row, col, dir):                           # 방향별 후진한 뒤의 좌표 return
    return go(row, col, (dir + 2) % 4)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
_map = []
for i in range(n):
    _map.append(list(map(int, input().split())))

cleaned = 0
clean(0)
print(cleaned)