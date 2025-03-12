import math
n,m = map(int, input().split())
_trees = list(map(int, input().split()))

_trees.sort(reverse=True)
arr = [[_trees[0],1]]
i = 1
while i < n:
    if arr[-1][0] == _trees[i]:
        arr[-1][1] += 1
        i += 1
    else:
        arr.append([_trees[i], 1]) 
        i += 1



if len(arr) == 1:
    h = arr[0][0] - math.ceil(m/arr[0][1])

    print(h)
else:
    c = 0
    i = 0
    h = arr[i][0]
    tmp = 0
    while i < len(arr)-1: 
        if tmp + (arr[i][0] - arr[i+1][0]) * (arr[i][1]+c) < m:
            tmp += (arr[i][0] - arr[i+1][0]) * (arr[i][1]+c)
            h -= (arr[i][0] - arr[i+1][0])
            c += arr[i][1]
            i += 1
        else:
            h -= math.ceil((m-tmp)/(arr[i][1]+c))
            tmp += math.ceil((m-tmp)/(arr[i][1]+c)) * (arr[i][1]+c)
            break

    if tmp >= m:
        print(h)
    else:
        h -= math.ceil((m-tmp)/(arr[i][1]+c))
        print(h)