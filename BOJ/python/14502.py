from copy import deepcopy


def bfs():  # bfs 탐색 함수 (바이러스 퍼지는 것을 구현)
    global tmap
    global q
    global contaminated

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        r, c = q.pop(0)
        for i in range(4):
            if 0 <= r + dr[i] <= n-1 and 0 <= c + dc[i] <= m-1 and tmap[r + dr[i]][c + dc[i]] == 0:
                tmap[r + dr[i]][c + dc[i]] = 2
                contaminated += 1
                q.append((r + dr[i], c + dc[i]))


# main
n, m = map(int, input().split())

# 맵 받아오기
lmap = []
for i in range(n):
    lmap.append(list(map(int, input().split())))

vspot = []  # 바이러스 존재 지점 저장
virus = 0  # 원래 맵에서 바이러스 존재지점
walls = 3  # 원래 맵에서 1인 것들의 갯수를 저장 -> 세개는 반드시 세우니까 default = 3

for row in range(n):
    for col in range(m):
        if lmap[row][col] == 2:
            vspot.append((row, col))
            virus += 1
        elif lmap[row][col] == 1:
            walls += 1

maxarea = 0

for i1 in range(n*m - 2):
    if lmap[int(i1/m)][i1 % m] == 0:
        pos1 = (int(i1/m), i1 % m)  # 첫번째 벽
        for i2 in range(i1+1, n*m - 1):
            if lmap[int(i2/m)][i2 % m] == 0:
                pos2 = (int(i2/m), i2 % m)  # 두번째 벽
                for i3 in range(i2+1, n*m):
                    if lmap[int(i3/m)][i3 % m] == 0:
                        pos3 = (int(i3/m), i3 % m)  # 세번째 벽

                        # 벽 세개가 세워진 한 케이스에 대해 바이러스 퍼뜨리고 안전영역 검사
                        # 원본인 lmap은 또 써야하니 복사본을 만든다
                        tmap = deepcopy(lmap)
                        tmap[pos1[0]][pos1[1]] = 1
                        tmap[pos2[0]][pos2[1]] = 1
                        tmap[pos3[0]][pos3[1]] = 1

                        # 바이러스 퍼뜨리는 부분
                        contaminated = 0  # 새롭게 오염된 부분
                        for v in vspot:
                            q = [v]
                            bfs()

                        # 안전영역 크기 검사
                        area = n*m - walls - virus - contaminated

                        # 최댓값 갱신
                        if area > maxarea:
                            maxarea = area

print(maxarea)