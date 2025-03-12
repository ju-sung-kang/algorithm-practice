from collections import deque

n=int(input())
mat=[list(map(int, input().split())) for _ in range(n)]

# 아기상어 시작위치
def shark_start_pos():
    for r in range(n):
        for c in range(n):
            if mat[r][c]==9:
                return (r,c)
            
# pos(r,c)로 이동가능한지
def can_move_to(pos, shark_size):
    r,c=pos
    return (0<=r<n and 0<=c<n and mat[r][c]<=shark_size)

# pos(r,c)의 물고기 먹는게 가능한지
def can_eat(pos, shark_size):
    r,c=pos
    return 0<mat[r][c]<shark_size
    

directions=[(-1,0), (0,-1), (0,1), (1,0)]
def bfs(pos, shark_size, total_time, eat_fish):
    visited=[[False]*n for _ in range(n)]
    r,c=pos

    q=deque([(r,c,0)])
    mat[r][c]=0 # 방문한 노드 숫자를 지운다
    visited[r][c]=True

    while q:
        r,c,d=q.popleft()
        # bfs를 돌다가 탐색한 노드에 먹을 수 있는 물고기가 있다면 더이상 bfs를 돌 필요가 없다
        # q에있는 같은 거리의 노드들을 전부 꺼내고 다음에 어떤 물고기를 잡아먹을지 검사한다
        if can_eat((r,c),shark_size):
            fish_list = [(r,c,d)]
            while q and q[0][2]==d: # q[0][2]=d
                _r,_c,_d=q.popleft()
                if can_eat((_r,_c),shark_size): fish_list.append((_r,_c,_d))

            # 가장 위, 그중 가장 왼쪽 물고기
            fish_list.sort()
            next_fish=fish_list[0]
            
            # 다음 희생 물고기가 결정되었다면 그 위치로 아기상어를 옮기고 다시 bfs를 반복한다
            # 이 과정에서 아기상어가 성장했는지 검사하고, 이동한 위치의 물고기 숫자는 0으로 변경해준다
            sizeup = (eat_fish + 1 == shark_size)

            return bfs(
                (next_fish[0], next_fish[1]),
                shark_size+1 if sizeup else shark_size,
                total_time+d,
                0 if sizeup else eat_fish+1
            )
        
        # 희생 물고기를 발견하지 못했다면 일반적인 bfs 인접노드 탐색
        for dr, dc in directions:
            nr,nc=r+dr,c+dc
            if can_move_to((nr,nc),shark_size) and not visited[nr][nc]:
                q.append((nr,nc,d+1))
                visited[nr][nc]=True
    
    # 여기로 왔다면 전부 탐색했는데 먹을 수 있는게 없었다는 얘기
    # 그럼 지금까지의 누적 시간을 계산한다
    return total_time

print(bfs(shark_start_pos(),2,0,0))