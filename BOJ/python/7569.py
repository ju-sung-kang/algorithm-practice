from collections import deque

dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

def in_range(z,y,x):
    if 0<=x<M and 0<=y<N and 0<=z<H:
        return True
    return False

def solve():
    q = deque()
    unripe = 0
    time = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if mat[z][y][x] == 1:
                    q.append((z,y,x,0))
                elif mat[z][y][x] == 0:
                    unripe += 1

    if unripe == 0:
        return 0

    while q:
        z,y,x,d = q.popleft()
        # 방문검사 거리검사
        for dz,dy,dx in dirs:
            nz,ny,nx = z+dz,y+dy,x+dx
            if not in_range(nz,ny,nx):
                continue
            if mat[nz][ny][nx] == 0:
                mat[nz][ny][nx] = 1
                q.append((nz,ny,nx,d+1))
                time = max(time, d+1)
                unripe -= 1

    return time if unripe == 0 else -1


M,N,H = map(int, input().split())
mat=[[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

print(solve())