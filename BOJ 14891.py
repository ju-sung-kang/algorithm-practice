def turn(g, d, flag):                       # 톱니돌리는 함수 flag가 -1:왼쪽/0:양 옆/+1:오른쪽 에 있는 톱니를 돌린다는 뜻
    if 0 < g and flag <= 0:                 # 왼쪽 톱니를 돌림
        if s[g-1][2] != s[g][6]:
            turn(g-1, d*(-1), -1)

    if g < 3 and flag >= 0:                 # 오른쪽 톱니를 돌림
        if s[g][2] != s[g+1][6]:
            turn(g+1, d*(-1), 1)

    if d == 1:                              # 시계방향 회전 (자기자신)
        s[g] = [s[g][7]] + s[g][:7]
    else:                                   # d == -1 반시계 방향 회전 (자기자신)
        s[g] = s[g][1:] + [s[g][0]]


s = [[],[],[],[]]
for i in range(4):
    tmp = input()
    for j in range(8):
        s[i].append(int(tmp[j]))

k = int(input())

for i in range(k):
    gear, dir = map(int, input().split())
    turn(gear-1, dir, 0)                    # 문제에서는 톱니번호 1~4로 주어진걸 0~3으로 바꿔서 썼음

ans = 0
for i in range(4):
    ans += s[i][0] * pow(2, i)

print(int(ans))
