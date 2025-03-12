def dfs(step, tmp_sum, pos):
    global max_sum
    global arr
    global n, m
    global visited

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    r, c = pos[0], pos[1]

    if step == 4:
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        return

    if max_val * (4 - step) + tmp_sum < max_sum:
        return

    for idx in range(4):
        next_r, next_c = r + dr[idx], c + dc[idx]
        if 0 <= next_r <= n - 1 and 0 <= next_c <= m - 1:
            if not visited[next_r][next_c]:
                visited[next_r][next_c] = True
                if step == 2:
                    dfs(step + 1, tmp_sum + arr[next_r][next_c], (r, c))  # T자 모양을 탐색하기 위한 부분
                dfs(step + 1, tmp_sum + arr[next_r][next_c], (next_r, next_c))
                visited[next_r][next_c] = False
    return


# main 실행 영역

n, m = map(int, input().split())
arr = [[0 for col in range(m)] for row in range(n)]
avg = 0
for i in range(n):
    arr[i] = list(map(int, input().split()))

# 평균과 최댓값을 구하기 위한 과정
max_val = 0
for i in range(n):
    for j in range(m):
        avg += arr[i][j]
        if arr[i][j] > max_val:
            max_val = arr[i][j]

if avg % (n * m) == 0:
    avg = avg / (n * m)
else:
    avg = avg // (n * m) + 1

# 최댓값 구하기

max_sum = 0
row = 0
col = 0

visited = [[False for _col in range(m)] for _row in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] >= avg:  # 최댓값을 구하는 것이므로 평균이 넘는 지점에서만 dfs를 돌아도 된다
            row = i
            col = j

            visited[row][col] = True
            dfs(1, arr[row][col], (row, col))
            visited[row][col] = False

# 결과출력

print(max_sum)
