n = int(input())
a = list(map(int, input().split()))

LIS = [a[0]]
index = [0] * n

for i in range(1,n):
    start = 0
    end = len(LIS) - 1
    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] > a[i]:
            end = mid - 1
        elif LIS[mid] == a[i]:
            start = mid
            break
        else:
            start = mid + 1

    if start >= len(LIS):
        LIS.append(a[i])
    else:
        LIS[start] = a[i]

    index[i] = start

cnt = len(LIS)-1
answer = ""
for i in range(n-1, -1, -1):
    if index[i] == cnt:
        answer = str(a[i]) + " " + answer
        cnt -= 1
        if cnt < 0: break

print(len(LIS))
print(answer)