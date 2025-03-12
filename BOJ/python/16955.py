mat = [str(input()) for _ in range(10)]

def inmat(r,c):
    if 0<=r<10 and 0<=c<10: return True
    else: return False


def answer():
    for r in range(10):
        for c in range(10):
            # check row -
            x=0
            dot=0
            for i in range(5):
                ri,ci=r,c+i
                if not inmat(ri, ci): break
                if mat[ri][ci] == 'X': x+=1
                if mat[ri][ci] == '.': dot+=1
            if x == 4 and dot == 1:
                return 1
                
            # check col |
            x=0
            dot=0
            for i in range(5):
                ri,ci=r+i,c
                if not inmat(ri, ci): break
                if mat[ri][ci] == 'X': x+=1
                if mat[ri][ci] == '.': dot+=1
            if x == 4 and dot == 1:
                return 1

            
            # check diagonal \
            x=0
            dot=0
            for i in range(5):
                ri, ci = r+i, c+i
                if not inmat(ri, ci): break
                if mat[ri][ci] == 'X': x+=1
                if mat[ri][ci] == '.': dot+=1
            if x == 4 and dot == 1:
                return 1
            
            
            # check diagonal /
            x=0
            dot=0
            for i in range(5):
                ri, ci = r-i, c+i
                if not inmat(ri, ci): break
                if mat[ri][ci] == 'X': x+=1
                if mat[ri][ci] == '.': dot+=1
            if x == 4 and dot == 1:
                return 1
            
    return 0
            
print(answer())