def union(v1, v2):
    global parent
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        parent[r2] = r1


def find(v):
    if parent[v] == v:
        return v
    else:
        return find(parent[v])


n = int(input())
m = int(input())
edge = []
for i in range(m):
    e1, e2, cost = map(int, input().split())
    edge.append((e1-1, e2-1, cost))

edge.sort(key=lambda x: x[2])

parent = [i for i in range(n)]

ans = 0
cnt = 0
for e1, e2, cost in edge:
    if find(e1) != find(e2):
        union(e1,e2)
        ans += cost
        cnt += 1
        if cnt == n-1: break

print(ans)
