import sys

n = int(sys.stdin.readline())
meet = []
for i in range(n):
    meet.append(list(map(int,sys.stdin.readline().split())))

meet.sort(key = lambda x: (x[1],x[0]))

e = 0
cnt = 0
for m in meet:
    if m[0] >= e:
        cnt += 1
        e = m[1]

print(cnt)