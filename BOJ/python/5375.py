'''
[ㅡ, 북, ㅡ]
[서, 밑, 동]
[ㅡ, 남, ㅡ]
[ㅡ, 위, ㅡ]
(흰색 w 0) (노란색 y 1) (빨간색 r 2) (오렌지색 o 3) (초록색 g 4) (파란색 b 5)
['w', 'y', 'r', 'o', 'g', 'b']
'''
from copy import deepcopy


def plane_rotate(arr, dir):  # 면을 회전하는 부분 처리
    tmp = deepcopy(arr)
    if dir == "+":
        arr[0][2] = tmp[0][0]
        arr[1][2] = tmp[0][1]
        arr[2][2] = tmp[0][2]

        arr[2][2] = tmp[0][2]
        arr[2][1] = tmp[1][2]
        arr[2][0] = tmp[2][2]

        arr[2][0] = tmp[2][2]
        arr[1][0] = tmp[2][1]
        arr[0][0] = tmp[2][0]

        arr[0][0] = tmp[2][0]
        arr[0][1] = tmp[1][0]
        arr[0][2] = tmp[0][0]
    else:  #  "-"
        arr[0][0] = tmp[0][2]
        arr[0][1] = tmp[1][2]
        arr[0][2] = tmp[2][2]

        arr[0][2] = tmp[2][2]
        arr[1][2] = tmp[2][1]
        arr[2][2] = tmp[2][0]

        arr[2][2] = tmp[2][0]
        arr[2][1] = tmp[1][0]
        arr[2][0] = tmp[0][0]

        arr[2][0] = tmp[0][0]
        arr[1][0] = tmp[0][1]
        arr[0][0] = tmp[0][2]



def u_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(u, dir)
    if dir == "+":
        tmp = deepcopy(f[0])
        f[0] = r[0]
        r[0] = b[0]
        b[0] = l[0]
        l[0] = tmp
    else:  # "-"
        tmp = deepcopy(f[0])
        f[0] = l[0]
        l[0] = b[0]
        b[0] = r[0]
        r[0] = tmp


def d_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(d, dir)
    if dir == "+":
        tmp = deepcopy(f[2])
        f[2] = l[2]
        l[2] = b[2]
        b[2] = r[2]
        r[2] = tmp
    else:  # "-"
        tmp = deepcopy(f[2])
        f[2] = r[2]
        r[2] = b[2]
        b[2] = l[2]
        l[2] = tmp


def f_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(f, dir)
    if dir == "+":
        tmp = [d[2][0], d[2][1], d[2][2]]
        d[2][0], d[2][1], d[2][2] = r[0][0], r[1][0], r[2][0]
        r[0][0], r[1][0], r[2][0] = u[2][0], u[2][1], u[2][2]
        u[2][0], u[2][1], u[2][2] = l[2][2], l[1][2], l[0][2]
        l[2][2], l[1][2], l[0][2] = tmp[0], tmp[1], tmp[2]
    else:  # "-"
        tmp = [d[2][0], d[2][1], d[2][2]]
        d[2][0], d[2][1], d[2][2] = l[2][2], l[1][2], l[0][2]
        l[2][2], l[1][2], l[0][2] = u[2][0], u[2][1], u[2][2]
        u[2][0], u[2][1], u[2][2] = r[0][0], r[1][0], r[2][0]
        r[0][0], r[1][0], r[2][0] = tmp[0], tmp[1], tmp[2]


def b_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(b, dir)
    if dir == "+":
        tmp = [d[0][2], d[0][1], d[0][0]]
        d[0][2], d[0][1], d[0][0] = l[0][0], l[1][0], l[2][0]
        l[0][0], l[1][0], l[2][0] = u[0][2], u[0][1], u[0][0]
        u[0][2], u[0][1], u[0][0] = r[2][2], r[1][2], r[0][2]
        r[2][2], r[1][2], r[0][2] = tmp[0], tmp[1], tmp[2]

    else:  # "-"
        tmp = [d[0][2], d[0][1], d[0][0]]
        d[0][2], d[0][1], d[0][0] = r[2][2], r[1][2], r[0][2]
        r[2][2], r[1][2], r[0][2] = u[0][2], u[0][1], u[0][0]
        u[0][2], u[0][1], u[0][0] = l[0][0], l[1][0], l[2][0]
        l[0][0], l[1][0], l[2][0] = tmp[0], tmp[1], tmp[2]


def l_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(l, dir)
    if dir == "+":
        tmp = [d[2][2], d[1][2], d[0][2]]
        d[2][2], d[1][2], d[0][2] = f[0][0], f[1][0], f[2][0]
        f[0][0], f[1][0], f[2][0] = u[0][0], u[1][0], u[2][0]
        u[0][0], u[1][0], u[2][0] = b[2][2], b[1][2], b[0][2]
        b[2][2], b[1][2], b[0][2] = tmp[0], tmp[1], tmp[2]
    else:  # "-"
        tmp = [d[2][2], d[1][2], d[0][2]]
        d[2][2], d[1][2], d[0][2] = b[2][2], b[1][2], b[0][2]
        b[2][2], b[1][2], b[0][2] = u[0][0], u[1][0], u[2][0]
        u[0][0], u[1][0], u[2][0] = f[0][0], f[1][0], f[2][0]
        f[0][0], f[1][0], f[2][0] = tmp[0], tmp[1], tmp[2]


def r_rotate(dir):
    global u, d, f, b, l, r
    plane_rotate(r, dir)
    if dir == "+":
        tmp = [d[0][0], d[1][0], d[2][0]]
        d[0][0], d[1][0], d[2][0] = b[0][0], b[1][0], b[2][0]
        b[0][0], b[1][0], b[2][0] = u[2][2], u[1][2], u[0][2]
        u[2][2], u[1][2], u[0][2] = f[2][2], f[1][2], f[0][2]
        f[2][2], f[1][2], f[0][2] = tmp[0], tmp[1], tmp[2]
    else:  # "-"
        tmp = [d[0][0], d[1][0], d[2][0]]
        d[0][0], d[1][0], d[2][0] = f[2][2], f[1][2], f[0][2]
        f[2][2], f[1][2], f[0][2] = u[2][2], u[1][2], u[0][2]
        u[2][2], u[1][2], u[0][2] = b[0][0], b[1][0], b[2][0]
        b[0][0], b[1][0], b[2][0] = tmp[0], tmp[1], tmp[2]


numtocolor = ['w', 'y', 'r', 'o', 'g', 'b']
T = int(input())
for case in range(T):
    u = [[0] * 3 for _0 in range(3)]
    d = [[1] * 3 for _1 in range(3)]
    f = [[2] * 3 for _2 in range(3)]
    b = [[3] * 3 for _3 in range(3)]
    l = [[4] * 3 for _4 in range(3)]
    r = [[5] * 3 for _5 in range(3)]

    n = int(input())
    rlist = list(map(str, input().split()))

    for rotation in rlist:
        if rotation[0] == "U":
            u_rotate(rotation[1])
        elif rotation[0] == "D":
            d_rotate(rotation[1])
        elif rotation[0] == "F":
            f_rotate(rotation[1])
        elif rotation[0] == "B":
            b_rotate(rotation[1])
        elif rotation[0] == "L":
            l_rotate(rotation[1])
        else:  # R
            r_rotate(rotation[1])
    for i in range(3):
        show = ""
        for j in range(3):
            show += numtocolor[u[i][j]]
        print(show)