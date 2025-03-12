def dotRotate(xypos, opos):  # opos: 회전의 중심점, xypos: 회전대상
    return opos[1] - xypos[1] + opos[0], xypos[0] - opos[0] + opos[1]


def dragonCurve(curg, generation, dclist):
    global dotmap

    if curg == generation:
        for posx, posy in dclist:
            if dotmap[posy][posx] == 0:
                dotmap[posy][posx] = 1
    else:
        tmp = []
        for i in range(len(dclist)-2, -1, -1):
            tmp.append(dotRotate(dclist[i], dclist[-1]))
        dclist += tmp
        dragonCurve(curg + 1, generation, dclist)


def squareCheck(pos):
    global dotmap
    global ans
    x, y = pos
    if dotmap[y][x] + dotmap[y+1][x] + dotmap[y][x+1] + dotmap[y+1][x+1] == 4:
        ans += 1


n = int(input())
dotmap = [[0 for col in range(101)] for row in range(101)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(n):
    x,y,d,g = map(int, input().split())
    dcl = [(x,y), (x+dx[d], y+dy[d])]
    dragonCurve(0, g, dcl)

ans = 0
for xi in range(100):
    for yi in range(100):
        squareCheck((xi, yi))

print(ans)
