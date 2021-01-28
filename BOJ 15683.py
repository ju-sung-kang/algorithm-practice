from copy import deepcopy


def cam1(row, col, case, omap):  # 1번 캠 감시영역 omap에 반영
    monitor(row, col, case, omap)


def cam2(row, col, case, omap):  # 2번 캠 감시영역 omap에 반영
    monitor(row, col, case, omap)
    monitor(row, col, case + 2, omap)


def cam3(row, col, case, omap):  # 3번 캠 감시영역 omap에 반영
    monitor(row, col, case, omap)
    monitor(row, col, (case + 1) % 4, omap)


def cam4(row, col, case, omap):  # 4번 캠 감시영역 omap에 반영
    monitor(row, col, (case + 3) % 4, omap)
    monitor(row, col, case, omap)
    monitor(row, col, (case + 1) % 4, omap)


def cam5(row, col, omap):  # 5번 캠 감시영역 omap에 반영
    for i in range(4):
        monitor(row, col, i, omap)


def monitor(row, col, dir, omap):  # (row,col)에서 dir방향으로 감시영역에 7 체크
    global n                       # 북 동 남 서 순으로 0 1 2 3
    global m

    if dir == 0:
        while row > 0:
            row -= 1
            if omap[row][col] == 6:  # wall
                break
            if omap[row][col] == 0:
                omap[row][col] = 7
    elif dir == 1:
        while col < m-1:
            col += 1
            if omap[row][col] == 6:
                break
            if omap[row][col] == 0:
                omap[row][col] = 7
    elif dir == 2:
        while row < n-1:
            row += 1
            if omap[row][col] == 6:
                break
            if omap[row][col] == 0:
                omap[row][col] = 7
    else:  # dir == 3:
        while col > 0:
            col -= 1
            if omap[row][col] == 6:
                break
            if omap[row][col] == 0:
                omap[row][col] = 7


def defineCam(list):  # 각 캠의 감시방향 list에 담기
    global campos
    global min_val
    global camnum

    if len(list) == camnum:  # 모든 캠의 감시방향 설정 완료시, 사각지대크기 최소값 업데이트
        ans = blindSpot(list)
        if ans < min_val:
            min_val = ans
    else:
        cam = campos.pop()
        if cam[2] == 2:  # 2번 캠은 두가지 케이스만 존재
            for i in range(2):
                defineCam(list + [(cam[0], cam[1], cam[2], i)])
        else:  # 나머지 캠은 (1,3,4) 네가지 케이스 존재
            for i in range(4):
                defineCam(list + [(cam[0], cam[1], cam[2], i)])
        campos.append(cam)


def blindSpot(list):  # list 에 담긴 캠의 감시방향에 따른 사각지대를 return
    global n, m
    global office

    omap = deepcopy(office)
    for x in list:
        if x[2] == 1:
            cam1(x[0], x[1], x[3], omap)
        elif x[2] == 2:
            cam2(x[0], x[1], x[3], omap)
        elif x[2] == 3:
            cam3(x[0], x[1], x[3], omap)
        elif x[2] == 4:
            cam4(x[0], x[1], x[3], omap)
        else:  # x[2] == 5:
            cam5(x[0], x[1], omap)

    bspot = 0
    for i in range(n):
        for j in range(m):
            if omap[i][j] == 0:
                bspot += 1

    return bspot


n, m = map(int, input().split())
office = []
for i in range(n):
    office.append(list(map(int, input().split())))

campos = []  # 5번 캠을 제외한 캠의 위치와 종류 목록
camnum = 0  # 5번 캠을 제외한 캠의 개수
cam5pos = []  # 5번 캠의 위치 목록
min_val = float('inf')
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 5:
            campos.append((i, j, office[i][j]))
            camnum += 1
        elif office[i][j] == 5:
            cam5pos.append((i, j))

for cam in cam5pos:  # 5번캠은 미리 감시영역 반영
    cam5(cam[0], cam[1], office)

defineCam([])  # 재귀호출 (dfs방식)으로 모든 캠의 감시방향 조합 각각을 탐색하며 min_val 찾기
print(min_val)
