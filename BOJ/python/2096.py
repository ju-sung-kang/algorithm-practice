import sys
n = int(sys.stdin.readline())
maxdp = list(map(int, sys.stdin.readline().split()))
mindp = maxdp[:]

for _ in range(n-1):
    a0,a1,a2 = map(int, sys.stdin.readline().split())
    tmp = maxdp[:]
    maxdp[0] = max(a0 + tmp[0], a0 + tmp[1])
    maxdp[1] = max(a1 + tmp[0], a1 + tmp[1], a1 + tmp[2])
    maxdp[2] = max(a2 + tmp[1], a2 + tmp[2])
    tmp = mindp[:]
    mindp[0] = min(a0 + tmp[0], a0 + tmp[1])
    mindp[1] = min(a1 + tmp[0], a1 + tmp[1], a1 + tmp[2])
    mindp[2] = min(a2 + tmp[1], a2 + tmp[2])

sys.stdout.write(str(max(maxdp)) + " " + str(min(mindp)))