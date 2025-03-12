from collections import deque
from typing import Tuple

N,M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
mat_visit = [[False] * M for _ in range(N)]

def bfs(pos: Tuple[int, int]):
    q = deque([pos])
    DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]
    size = 0
    while q:
        row, col = q.popleft()
        if mat_visit[row][col]: continue
        
        mat_visit[row][col] = True
        size += 1

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc
            if (
                0<=nr<N and 0<=nc<M
                and mat[nr][nc] == 1
                and not mat_visit[nr][nc]
            ):
                q.append((nr, nc))
    
    return size

NUM_PICTURES = 0
MAX_SIZE = 0

for r in range(N):
    for c in range(M):
        if mat[r][c] and not mat_visit[r][c]:
            size = bfs((r,c))
            MAX_SIZE = max(MAX_SIZE, size)
            NUM_PICTURES += 1

print(NUM_PICTURES)
print(MAX_SIZE)