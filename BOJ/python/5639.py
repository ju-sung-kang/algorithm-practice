import sys
sys.setrecursionlimit(10**9)

def func(s,e):
    global tree
    if s == e:
        print(tree[s])
        return
    rs = s+1
    find = False
    start = s+1
    end = e
    while start <= end:
        mid = (start + end) // 2
        if tree[mid] > tree[s]:
            if tree[mid-1] < tree[s]:
                rs = mid
                find = True
                break
            else:
                end = mid - 1
        else:
            start = mid + 1

    if find:
        func(s+1, rs-1)
        func(rs, e)
    else:
        if s+1 <= e:
            func(s+1,e)
    # root
    print(tree[s])

tree = []
while True:
    try:
        tree.append(int(sys.stdin.readline()))
    except:
        break

func(0, len(tree)-1)