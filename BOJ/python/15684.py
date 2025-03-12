def check():
    global arr
    global n,h

    for start in range(n):
        cur = start
        for i in range(h):
            if cur > 0 and arr[i][cur-1]:
                cur -= 1
            elif cur < n-1 and arr[i][cur]:
                cur += 1
        if cur != start:
            return False
    return True


def dfs(cnt, row, col):
    global arr
    global ans
    global n,h

    if cnt > 3:
        return
    elif check() and cnt < ans:
        ans = cnt
    else:
        for r in range(row, h):
            if row == r: ncol = col
            else: ncol = 0
            for c in range(ncol, n-1):
                if not arr[r][c]:
                    if n == 2:
                        arr[r][c] = True
                        dfs(cnt+1, r+1, c)
                        arr[r][c] = False
                    elif c == n-2:
                        arr[r][c] = True
                        dfs(cnt + 1, r, c + 2)
                        arr[r][c] = False
                    else:
                        if not arr[r][c+1]:
                            arr[r][c] = True
                            dfs(cnt+1, r, c + 2)
                            arr[r][c] = False


n, m, h = map(int, input().split())
arr = [[False for col in range(n-1)] for row in range(h)]
ans = 4
for i in range(m):
    a, b = map(int, input().split())
    arr[a-1][b-1] = True

if n == 2:
    if m % 2 == 0:
        print(0)
    else:
        print(1)
elif m == 1:
    print(1)
elif check():
    print(0)
else:
    dfs(0,0,0)
    if ans == 4:
        print(-1)
    else:
        print(ans)
