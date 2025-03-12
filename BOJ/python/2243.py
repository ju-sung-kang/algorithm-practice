import sys


def fixcandy(lv, num):
    global tree, c
    tree[c+lv] += num
    cur = c+lv
    while cur > 0:
        parent = cur//2
        tree[parent] += num
        cur = parent


def findcandy(order):
    global tree, c
    cur = 1
    while cur <= c:
        left = 2*cur
        right = 2*cur + 1
        if order <= tree[left]:
            cur = left
        else:
            cur = right
            order -= tree[left]
    print(cur-c)
    fixcandy(cur-c, -1)


tree = [0] * 2097152  # 2^21
c = 1048575  # 2^20-1
n = int(sys.stdin.readline())
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))

    if tmp[0] == 1:
        findcandy(tmp[1])
    else:  # tmp[0] == 2
        fixcandy(tmp[1],tmp[2])