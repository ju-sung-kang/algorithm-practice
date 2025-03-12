N = int(input())
x = list(map(int, input().split()))

x_sorted = sorted(set(x))
ans = []

for xi in x:
    l, r = 0, len(x_sorted)-1
    while l < r:
        mid = (l+r)//2
        if x_sorted[mid] < xi:
            l = mid + 1
        else:
            r = mid
    ans.append(str(l))

print(" ".join(ans))