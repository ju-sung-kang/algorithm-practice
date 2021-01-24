from copy import deepcopy


def left(step, nmap, redpos, bluepos):
    global min_val

    goal = 0
    if step <= 10:
        tmap = deepcopy(nmap)
        rpos = deepcopy(redpos)
        bpos = deepcopy(bluepos)
        while True:
            if tmap[rpos[0]][rpos[1]-1] == 0:
                tmap[rpos[0]][rpos[1]] = 0
                tmap[rpos[0]][rpos[1]-1] = 2
                rpos[1] -= 1
            elif tmap[rpos[0]][rpos[1]-1] == 1:
                break
            elif tmap[rpos[0]][rpos[1]-1] == 3:
                break
            else:  # 4
                goal = 2
                tmap[rpos[0]][rpos[1]] = 0
                break

        while True:
            if tmap[bpos[0]][bpos[1]-1] == 0:
                tmap[bpos[0]][bpos[1]] = 0
                tmap[bpos[0]][bpos[1]-1] = 3
                bpos[1] -= 1
            elif tmap[bpos[0]][bpos[1]-1] == 1:
                break
            elif tmap[bpos[0]][bpos[1]-1] == 2:
                break
            else:  # 4
                goal = 3
                break

        if goal == 0:
            while True:
                if tmap[rpos[0]][rpos[1]-1] == 0:
                    tmap[rpos[0]][rpos[1]] = 0
                    tmap[rpos[0]][rpos[1]-1] = 2
                    rpos[1] -= 1
                elif tmap[rpos[0]][rpos[1]-1] == 1:
                    break
                elif tmap[rpos[0]][rpos[1]-1] == 3:
                    break
                else:  # 4
                    goal = 2
                    break

        if goal == 0:
            up(step + 1, tmap, rpos, bpos)
            down(step + 1, tmap, rpos, bpos)

        else:
            if goal == 2:
                if step < min_val:
                    min_val = step


def right(step, nmap, redpos, bluepos):
    global min_val

    goal = 0
    if step <= 10:
        tmap = deepcopy(nmap)
        rpos = deepcopy(redpos)
        bpos = deepcopy(bluepos)
        while True:
            if tmap[rpos[0]][rpos[1]+1] == 0:
                tmap[rpos[0]][rpos[1]] = 0
                tmap[rpos[0]][rpos[1]+1] = 2
                rpos[1] += 1
            elif tmap[rpos[0]][rpos[1]+1] == 1:
                break
            elif tmap[rpos[0]][rpos[1]+1] == 3:
                break
            else:  # 4
                goal = 2
                tmap[rpos[0]][rpos[1]] = 0
                break

        while True:
            if tmap[bpos[0]][bpos[1]+1] == 0:
                tmap[bpos[0]][bpos[1]] = 0
                tmap[bpos[0]][bpos[1]+1] = 3
                bpos[1] += 1
            elif tmap[bpos[0]][bpos[1]+1] == 1:
                break
            elif tmap[bpos[0]][bpos[1]+1] == 2:
                break
            else:  # 4
                goal = 3
                break

        if goal == 0:
            while True:
                if tmap[rpos[0]][rpos[1]+1] == 0:
                    tmap[rpos[0]][rpos[1]] = 0
                    tmap[rpos[0]][rpos[1]+1] = 2
                    rpos[1] += 1
                elif tmap[rpos[0]][rpos[1]+1] == 1:
                    break
                elif tmap[rpos[0]][rpos[1]+1] == 3:
                    break
                else:  # 4
                    goal = 2
                    break

        if goal == 0:
            up(step + 1, tmap, rpos, bpos)
            down(step + 1, tmap, rpos, bpos)

        else:
            if goal == 2:
                if step < min_val:
                    min_val = step


def up(step, nmap, redpos, bluepos):
    global min_val

    goal = 0
    if step <= 10:
        tmap = deepcopy(nmap)
        rpos = deepcopy(redpos)
        bpos = deepcopy(bluepos)
        while True:
            if tmap[rpos[0]-1][rpos[1]] == 0:
                tmap[rpos[0]][rpos[1]] = 0
                tmap[rpos[0]-1][rpos[1]] = 2
                rpos[0] -= 1
            elif tmap[rpos[0]-1][rpos[1]] == 1:
                break
            elif tmap[rpos[0]-1][rpos[1]] == 3:
                break
            else:  # 4
                goal = 2
                tmap[rpos[0]][rpos[1]] = 0
                break

        while True:
            if tmap[bpos[0]-1][bpos[1]] == 0:
                tmap[bpos[0]][bpos[1]] = 0
                tmap[bpos[0]-1][bpos[1]] = 3
                bpos[0] -= 1
            elif tmap[bpos[0]-1][bpos[1]] == 1:
                break
            elif tmap[bpos[0]-1][bpos[1]] == 2:
                break
            else:  # 4
                goal = 3
                break

        if goal == 0:
            while True:
                if tmap[rpos[0]-1][rpos[1]] == 0:
                    tmap[rpos[0]][rpos[1]] = 0
                    tmap[rpos[0]-1][rpos[1]] = 2
                    rpos[0] -= 1
                elif tmap[rpos[0]-1][rpos[1]] == 1:
                    break
                elif tmap[rpos[0]-1][rpos[1]] == 3:
                    break
                else:  # 4
                    goal = 2
                    break

        if goal == 0:
            left(step + 1, tmap, rpos, bpos)
            right(step + 1, tmap, rpos, bpos)

        else:
            if goal == 2:
                if step < min_val:
                    min_val = step


def down(step, nmap, redpos, bluepos):
    global min_val

    goal = 0
    if step <= 10:
        tmap = deepcopy(nmap)
        rpos = deepcopy(redpos)
        bpos = deepcopy(bluepos)
        while True:
            if tmap[rpos[0]+1][rpos[1]] == 0:
                tmap[rpos[0]][rpos[1]] = 0
                tmap[rpos[0]+1][rpos[1]] = 2
                rpos[0] += 1
            elif tmap[rpos[0]+1][rpos[1]] == 1:
                break
            elif tmap[rpos[0]+1][rpos[1]] == 3:
                break
            else:  # 4
                goal = 2
                tmap[rpos[0]][rpos[1]] = 0
                break

        while True:
            if tmap[bpos[0]+1][bpos[1]] == 0:
                tmap[bpos[0]][bpos[1]] = 0
                tmap[bpos[0]+1][bpos[1]] = 3
                bpos[0] += 1
            elif tmap[bpos[0]+1][bpos[1]] == 1:
                break
            elif tmap[bpos[0]+1][bpos[1]] == 2:
                break
            else:  # 4
                goal = 3
                break

        if goal == 0:
            while True:
                if tmap[rpos[0]+1][rpos[1]] == 0:
                    tmap[rpos[0]][rpos[1]] = 0
                    tmap[rpos[0]+1][rpos[1]] = 2
                    rpos[0] += 1
                elif tmap[rpos[0]+1][rpos[1]] == 1:
                    break
                elif tmap[rpos[0]+1][rpos[1]] == 3:
                    break
                else:  # 4
                    goal = 2
                    break

        if goal == 0:
            left(step + 1, tmap, rpos, bpos)
            right(step + 1, tmap, rpos, bpos)

        else:
            if goal == 2:
                if step < min_val:
                    min_val = step


n, m = map(int, input().split())
str_map = []
_nmap = [[0 for col in range(m)] for row in range(n)]

for i in range(n):
    str_map.append(input())

_redpos = [0,0]
_bluepos = [0,0]
min_val = 11
for i in range(n):
    for j in range(m):
        if str_map[i][j] == "#":
            _nmap[i][j] = 1
        elif str_map[i][j] == ".":
            _nmap[i][j] = 0
        elif str_map[i][j] == "R":
            _nmap[i][j] = 2
            _redpos = [i, j]
        elif str_map[i][j] == "B":
            _nmap[i][j] = 3
            _bluepos = [i, j]
        else:  # str_map[i][j] == "O"
            _nmap[i][j] = 4


left(1, _nmap, _redpos, _bluepos)
right(1, _nmap, _redpos, _bluepos)
up(1, _nmap, _redpos, _bluepos)
down(1, _nmap, _redpos, _bluepos)

if min_val == 11:
    print(-1)
else:
    print(min_val)
