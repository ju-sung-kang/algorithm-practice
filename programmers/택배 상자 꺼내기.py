def find_position(w, box_num):
    # find position of box 
    direction = ((box_num-1)//w)%2 #extending direction 0:R 1:L
    top_floor_box = w if box_num%w==0 else box_num%w 
    bx = (w - top_floor_box + 1) if direction else top_floor_box
    by = box_num // w + 1 if (box_num % w) else 0
    return bx, by, direction
    

def solution(n, w, num): # n: 총상자 w: 가로개수 num: 꺼낼상자번호
    fx, fy, fdir = find_position(w, n)
    tx, ty, tdir = find_position(w, num)
    #print('fx', fx, 'fy', fy, 'fdir', fdir, 'tx', tx, 'ty', ty, 'tdir')
    roof_flag = None
    if fdir == tdir == 0 and tx <= fx: roof_flag = True
    elif fdir == tdir == 1 and fx <= tx: roof_flag = True
    elif fdir == 0 and tdir == 1 and fx >= tx: roof_flag = True
    elif fdir == 1 and tdir == 0 and fx <= tx: roof_flag = True
    else: roof_flag = False
    answer = fy - ty + 1 if roof_flag else fy - ty
    return answer

print(solution(22, 6, 8))