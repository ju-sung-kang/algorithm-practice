def rotation(cur_dir, to_where):
    if cur_dir == "up":
        if to_where > 0:
            return "right"
        else:
            return "left"
    elif cur_dir == "right":
        if to_where > 0:
            return "down"
        else:
            return "up"
    if cur_dir == "down":
        if to_where > 0:
            return "left"
        else:
            return "right"
    else:  # cur_dir == "left":
        if to_where > 0:
            return "up"
        else:
            return "down"


n = int(input())


#  벽과 뱀을 -1 빈곳을 0 사과를 1로 표현한 맵을 생성한다
gmap = [[0 for col in range(n+2)] for row in range(n+2)]  # 사과 위치, 뱀위치 등 게임용 map
for i in range(n+2):
    if i == 0 or i == n+1:
        for j in range(n+2):
            gmap[i][j] = -1  # -1은 벽 or 뱀을 의미
    else:
        gmap[i][0] = -1
        gmap[i][n+1] = -1

dmap = [[0 for col in range(n+2)] for row in range(n+2)]  # 방향을 기록해두는 map
dmap[1][1] = 1

k = int(input())

for i in range(k):
    ar, ac = map(int, input().split())
    gmap[ar][ac] = 1  # 1은 사과를 의미


# 방향을 받는다
l = int(input())

direction = []
for i in range(l):
    x, c = map(str, input().split())
    if c == "L":
        direction.append((-1) * int(x))  # 음수이면 왼쪽
    else:
        direction.append(int(x))  # 양수이면 오른쪽

dir_to_row = {"up":-1, "right":0, "down":1, "left":0}
dir_to_col = {"up":0, "right":1, "down":0, "left":-1}
num_to_dir = ["up", "right", "down", "left"]
dir_to_num = {"up": 0, "right": 1, "down": 2, "left": 3}

cur_head = [1, 1]
cur_tail = [1, 1]

cur_dir = "right"

time = 0

while True:
    time += 1
    cur_head[0] += dir_to_row[cur_dir]
    cur_head[1] += dir_to_col[cur_dir]

    if gmap[cur_head[0]][cur_head[1]] == 1:  # 전방에 사과
        gmap[cur_head[0]][cur_head[1]] = -1

    elif gmap[cur_head[0]][cur_head[1]] == 0:  # 전방에 아무것도 없음
        gmap[cur_head[0]][cur_head[1]] = -1
        gmap[cur_tail[0]][cur_tail[1]] = 0

        tmp_dir = num_to_dir[dmap[cur_tail[0]][cur_tail[1]]]  # 어떤 방향으로 꼬리가 줄어들지를 dmap에서 가져와서 반영함
        cur_tail[0] += dir_to_row[tmp_dir]
        cur_tail[1] += dir_to_col[tmp_dir]

    else: break # 벽이나 몸에 부딪힘

    if len(direction) > 0 and time == abs(direction[0]):
        cur_dir = rotation(cur_dir, direction[0])
        direction = direction[1:]

    dmap[cur_head[0]][cur_head[1]] = dir_to_num[cur_dir]

    #print("cur head: %d %d  cur tail: %d %d" %(cur_head[0], cur_head[1], cur_tail[0], cur_tail[1]))

print(time)




