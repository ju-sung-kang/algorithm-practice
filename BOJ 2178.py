import sys
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]
ans = 0

n, m = map(int, sys.stdin.readline().split())
arr = []
check = [[False]*m for row in range(n)]
check[0][0] = True
for _ in range(n):
    arr.append(sys.stdin.readline())

q = deque()
q.append((0,0,1))
while q:
    r,c,step = q.popleft()
    if r==n-1 and c==m-1:
        ans = step
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<n and 0<=nc<m:
            if not check[nr][nc] and arr[nr][nc] == '1':
                check[nr][nc] = True
                q.append((nr,nc,step+1))
print(ans)