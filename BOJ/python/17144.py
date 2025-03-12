# 입력
import sys
R,C,T=map(int, sys.stdin.readline().split())
mat=[list(map(int, sys.stdin.readline().split())) for _ in range(R)]

# 청정기 위치 찾아두기
m1,m2=None, None
for r in range(R):
    if mat[r][0]==-1:
        m1,m2=(r,0),(r+1,0)
        break

# 청정기 작동
# 시계방향순환시 반시계방향으로 탐색하며 다음값을 현재위치에 넣음
# 반시계방향순환시 시계방향으로 탐색하며 다음값을 현재위치에 넣음
COUNTER_CLOCK_DIRS=[(1,0),(0,1),(-1,0),(0,-1)]
CLOCK_DIRS=[(-1,0),(0,1),(1,0),(0,-1)]
def circulate(start, circulate_dir): # circulate_dir = -1 반시계, 1 시계
    dirs=CLOCK_DIRS if circulate_dir==-1 else COUNTER_CLOCK_DIRS
    row_range=(0,start[0]+1) if circulate_dir==-1 else (start[0],R)
    di=0
    dr,dc=dirs[di]
    r,c=start[0]+dr, start[1]+dc
    while True:
        nr,nc=None,None
        if row_range[0]<=r+dr<row_range[1] and 0<=c+dc<C: #범위 안에선 기존방향으로 진행
            nr,nc=r+dr,c+dc
        else: # 범위나갔으면 방향변경
            di+=1
            dr,dc=dirs[di]
            nr,nc=r+dr,c+dc
        
        if mat[nr][nc] == -1: # 청정기 앞에 도착했다면 0되고 종료
            mat[r][c]=0
            break
        else: # 그게 아니면 그 앞에 숫자를 현재위치에 넣음
            mat[r][c]=mat[nr][nc]
        
        r,c=nr,nc


# 1초에 한번 미세먼지가 확산됨
# 따로 배열을 하나두고, 각 위치에 얼만큼의 미세먼지가 더해지는지만 계산해둠
# 참고로 확산되어 감소된 원래 위치의 미세먼지는 별도의 배열에 적용하나, 바로적용하나 똑같음
for t in range(T):
    dif=[[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 숫자 발견 시 확산 진행
            if mat[r][c]>0:
                for dr,dc in CLOCK_DIRS: # 이건 시계/반시계 상관없음
                    nr,nc=r+dr,c+dc
                    if 0<=nr<R and 0<=nc<C and 0<=mat[nr][nc]:
                        dif[r][c]-=mat[r][c]//5
                        dif[nr][nc]+=mat[r][c]//5
    # 확산 변동값을 반영
    for r in range(R):
        for c in range(C):
            mat[r][c]+=dif[r][c]
    
    # 공기청정기 작동
    circulate(m1, -1)
    circulate(m2, 1)


# 반복문 종료 미세먼지 총량 출력
ans=0
for r in range(R):
    for c in range(C):
        if mat[r][c]>0: ans+= mat[r][c]

sys.stdout.write(f'{ans}\n')