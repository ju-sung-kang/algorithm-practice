from collections import deque
from itertools import combinations
import sys

n,m,k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    tmp = list(sys.stdin.readline())
    tmp.pop()
    arr.append(list(map(int,tmp)))


dr = [1,-1,0,0]
dc = [0,0,1,-1]

ans = 0

check = [[[False]*(k+1) for col in range(m)] for row in range(n)]
# 갈수있는지 체크
q = deque()
q.append((0,0,1,0))
check[0][0][0] = True
while q:
    r,c,d,w = q.popleft()
    if r == n-1 and c == m-1:
        ans = d
        break
    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        if 0<=nr<n and 0<=nc<m:
            if arr[nr][nc] == 0 and not check[nr][nc][w]:
                check[nr][nc][w] = True
                q.append((nr,nc,d+1,w))
            elif w < k and not check[nr][nc][w+1]:
                check[nr][nc][w+1] = True
                q.append((nr,nc,d+1,w+1))


if ans == 0:
    print(-1)
else:
    print(ans)
