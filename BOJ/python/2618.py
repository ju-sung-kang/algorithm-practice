from collections import deque


def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def bfs():
    global d
    global case, q

    while q:
        r, c, s = q.popleft()
        if r == w or c == w:
            print(str(d[0][0]) + '\n' + s)
            break
        else:
            next = max(r,c)+1
            if r==0 and c==0:
                if d[next][c] + distance(case[next], (0,0)) <= d[r][next] + distance(case[next], (n-1,n-1)):
                    q.append((next,c,s+"1\n"))
                else:
                    q.append((r,next,s+"2\n"))
            elif r == 0:
                if d[next][c] + distance(case[next], (0,0)) <= d[r][next] + distance(case[next], case[c]):
                    q.append((next,c,s+"1\n"))
                else:
                    q.append((r,next,s+"2\n"))
            elif c == 0:
                if d[next][c] + distance(case[next], case[r]) <= d[r][next] + distance(case[next], (n-1,n-1)):
                    q.append((next,c,s+"1\n"))
                else:
                    q.append((r,next,s+"2\n"))
            else:
                if d[next][c] + distance(case[next], case[r]) <= d[r][next] + distance(case[next], case[c]):
                    q.append((next,c,s+"1\n"))
                else:
                    q.append((r,next,s+"2\n"))


n = int(input())
w = int(input())
d = [[0]*(w+1) for _0 in range(w+1)]
p1 = [[(0,0)]*(w+1) for _1 in range(w+1)]
p2 = [[(n-1,n-1)]*(w+1) for _2 in range(w+1)]
case = [(0,0)]
for i in range(w):
    row, col = map(int, input().split())
    case.append((row-1,col-1))

for r in range(w, -1, -1):
    for c in range(w, -1, -1):
        if r == c and r != 0:
            d[r][c] = -1
        elif r == w or c == w:
            d[r][c] = 0
        else:
            next = max(r, c) + 1
            if r == 0 and c == 0:
                d[r][c] = min(d[next][c] + distance(case[next], (0,0)), d[r][next] + distance(case[next], (n-1,n-1)))
            elif r == 0:
                d[r][c] = min(d[next][c] + distance(case[next], (0,0)), d[r][next] + distance(case[next], case[c]))
            elif c == 0:
                d[r][c] = min(d[next][c] + distance(case[next], case[r]), d[r][next] + distance(case[next], (n-1,n-1)))
            else:
                d[r][c] = min(d[next][c] + distance(case[next], case[r]), d[r][next] + distance(case[next], case[c]))


q = deque()
q.append((0,0,""))
bfs()