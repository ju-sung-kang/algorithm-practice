from collections import deque

n,m,v = map(int, input().split())
adj = {i: [] for i in range(1,n+1)}

for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

for i in range(1,n+1):
    adj[i].sort()


def bfs(node):
    visited = [False] * (n+1)
    q = deque([node])
    path = []
    while q:
        cur = q.popleft()
        if visited[cur]: continue

        visited[cur] = True
        path.append(cur)

        if not adj[cur]: continue

        for a in adj[cur]:
            if visited[a]: continue

            q.append(a)

    return path

def dfs(node):
    s = [node]
    visited = [False] * (n+1)
    path = []
    while s:
        cur = s.pop()
        if visited[cur]: continue

        visited[cur] = True
        path.append(cur)

        if not adj[cur]: continue

        for a in reversed(adj[cur]):
            if visited[a]: continue
           
            s.append(a)

    return path

print(" ".join(map(str, dfs(v))))
print(" ".join(map(str, bfs(v))))
