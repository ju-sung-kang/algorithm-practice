import sys

# 0 출발이나 아무것도 없음 / 1 출구 / 2 묘비 / 3 귀신구멍 입구
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        gmap = [[0]*w for row in range(h)]
        dis = [[float("inf")]*w for row in range(h)]
        dis[0][0] = 0
        edges = []
        gmap[h-1][w-1] = 1  # 출구

        g = int(input())
        for _ in range(g):
            x, y = map(int, sys.stdin.readline().split())
            gmap[y][x] = 2  # 묘비

        e = int(input())
        for _ in range(e):
            x1, y1, x2, y2, t = map(int, sys.stdin.readline().split())
            gmap[y1][x1] = 3  # 귀신구멍 입구
            edges.append((y1, x1, y2, x2, t))

        for r in range(h):
            for c in range(w):
                if gmap[r][c] == 0:
                    if r>0:
                        if gmap[r-1][c] != 2:
                            edges.append((r,c,r-1,c,1))
                    if r<h-1:
                        if gmap[r+1][c] != 2:
                            edges.append((r,c,r+1,c,1))
                    if c>0:
                        if gmap[r][c-1] != 2:
                            edges.append((r,c,r,c-1,1))
                    if c<w-1:
                        if gmap[r][c+1] != 2:
                            edges.append((r,c,r,c+1,1))

        cycle = False
        for v in range(w*h-g+1):
            for edge in edges:
                if dis[edge[0]][edge[1]] < float("inf") and dis[edge[0]][edge[1]] + edge[4] < dis[edge[2]][edge[3]]:
                    dis[edge[2]][edge[3]] = dis[edge[0]][edge[1]] + edge[4]
                    if v == w*h-g:
                        cycle = True

        if cycle:
            print("Never")
        elif dis[h-1][w-1] < float("inf"):
            print(dis[h-1][w-1])
        else:
            print("Impossible")