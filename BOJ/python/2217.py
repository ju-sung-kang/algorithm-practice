import sys

n = int(sys.stdin.readline())
t = []
for _ in range(n):
    t.append(int(sys.stdin.readline()))

t.sort()
ans = 0
for i in range(n):
    ans = max(t[i]*(n-i), ans)

print(ans)