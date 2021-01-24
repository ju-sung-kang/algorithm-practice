n = int(input())
arr = list(map(int,input().split()))
m, v = map(int,input().split())
total = 0
for i in range(n):
    if arr[i] > m and (arr[i]-m) % v == 0:
        total += int((arr[i]-m) / v)
    elif arr[i] > m and (arr[i]-m) % v != 0:
        total += int((arr[i]-m) / v) + 1
total += n
print(total)
