import sys
n,m=map(int, input().split())
adj={i: [] for i in range(1, n+1)}
for _ in range(m):
    v1,v2=map(int, sys.stdin.readline().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

visit = [False]*(n+1)

def dfs_iterative(start):
    if visit[start]:
        return
    
    s = [start]
    while s:
        v = s.pop()
        visit[v] = True
        for nv in adj[v]:
            if visit[nv]:
                continue
            else:
                s.append(nv)

cnt = 0
for start in range(1,n+1):
    if not visit[start]:
        dfs_iterative(start)
        cnt += 1

print(cnt)