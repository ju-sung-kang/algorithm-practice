def dfs(curnode, curbitmask):
    global dp
    global cost

    if curbitmask == (1<<n) - 1:
        return cost[curnode][0] if cost[curnode][0] > 0 else float("inf")
    if dp[curnode][curbitmask] > 0:
        return dp[curnode][curbitmask]

    tmp = float("inf")
    for nextnode in range(1,n):
        if (curbitmask>>nextnode) % 2 == 0 and cost[curnode][nextnode]>0:
            tmp = min(tmp, cost[curnode][nextnode] + dfs(nextnode, curbitmask | (1<<nextnode)))
    dp[curnode][curbitmask] = tmp
    return tmp

n = int(input())
cost = [[0]*n for row1 in range(n)]
dp = [[0]*(1<<n) for row2 in range(n)]
for i in range(n):
    cost[i] = list(map(int, input().split()))

print(dfs(0, 1))