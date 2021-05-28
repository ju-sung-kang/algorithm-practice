import sys
from copy import copy

n = int(sys.stdin.readline())

alist = [0]*101
blist = [0]*101
for r in range(1,n+1):
    ain, bin = map(int, sys.stdin.readline().split())
    alist[ain]+=1
    blist[bin]+=1

    tmpa = copy(alist)
    tmpb = copy(blist)

    ans = 0
    a = 1
    b = 100
    while True:
        if a > 100 or b < 1:
            break

        if tmpa[a]>0 and tmpb[b]>0:
            ans = max(ans, a+b)

        if tmpa[a] == tmpb[b]:
            a += 1
            b -= 1
        elif tmpa[a] > tmpb[b]:
            tmpa[a] -= tmpb[b]
            b -= 1
        else:  # tmpa[a] < tmpb[b]
            tmpb[b] -= tmpa[a]
            a += 1

    sys.stdout.write(str(ans)+'\n')