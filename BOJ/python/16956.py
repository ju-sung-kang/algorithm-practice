def in_range(pos, R,C):
    _r,_c = pos
    if 0<=_r<R and 0<=_c<C:
        return True
    return False

R,C = map(int, input().split())
mat = [list(input()) for _ in range(R)]

def answer():
    DIRS = [(1,0), (-1,0), (0,-1), (0,1)]
    for row in range(R):
        for col in range(C):
            if mat[row][col] == "W":
                for dr, dc in DIRS:
                    nr, nc = row+dr, col+dc
                    if not in_range((nr, nc), R, C): continue
                    if mat[nr][nc] == "S":
                        return False
                    elif mat[nr][nc] == '.':
                        mat[nr][nc] = 'D'
    return True

if answer():
    print(1)
    for row in mat:
        print("".join(row))
else:
    print(0)
                    


