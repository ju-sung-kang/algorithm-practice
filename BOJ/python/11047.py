n, k = map(int, input().split())
values = []
for i in range(n):
    value = int(input())
    values.append(value)
    if value > k: continue

values.sort(reverse=True)
cnt = 0
for value in values:
    if k < value: continue
    cnt += k // value
    k %= value
    if k==0: break


print(cnt)