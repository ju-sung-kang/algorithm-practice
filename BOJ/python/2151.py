from collections import deque


def bfs(x,y,num,direction):
    global ans

    q = deque()
    q.append((x,y,num,direction))
    while q:
        r,c,m,d = q.popleft()
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<n and 0<=nc<n:
            if mir[nr][nc][d] > m:
                mir[nr][nc][d] = m
                if arr[nr][nc] == "!":
                    q.append((nr,nc,m,d))
                    q.append((nr,nc,m+1,(d+1)%4))
                    q.append((nr,nc,m+1,(d-1)%4))
                elif arr[nr][nc] == ".":
                    q.append((nr,nc,m,d))
                elif arr[nr][nc] == "#" and (nr,nc) == door[1]:
                    if ans > m: ans = m


dr = [-1,0,1,0]
dc = [0,1,0,-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

mir = [[[250]*4 for div1 in range(n)] for div2 in range(n)]

door = []
for row in range(n):
    for col in range(n):
        if arr[row][col] == "#":
            door.append((row,col))

ans = 250
for i in range(4):
    nr = door[0][0] + dr[i]
    nc = door[0][1] + dc[i]
    if 0<=nr<n and 0<=nc<n:
        if arr[nr][nc] != "*":
            bfs(door[0][0],door[0][1],0,i)

print(ans)
