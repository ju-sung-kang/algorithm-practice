import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    x1, x2 = map(int, sys.stdin.readline().split())
    if x1 <= x2:
        arr.append((x1, x2))
    else:
        arr.append((x2, x1))

arr.sort(key = lambda x: x[0])

end, ans = -1000000001, 0
for a, b in arr:
    if a >= end:
        ans += (b - a)
        end = b
    elif b > end:
        ans += (b - end)
        end = b

print(ans)