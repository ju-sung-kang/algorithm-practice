n = int(input())
dmap = [0]  # 일수저장
pmap = [0]  # 수익저장
for i in range(n):
    d, p = map(int, input().split())
    dmap.append(d)
    pmap.append(p)

dp = [0]*(n+2)

for i in range(1, n+1):
    if i + dmap[i] <= n+1:
        if dp[i] + pmap[i] > dp[i + dmap[i]]:
            dp[i + dmap[i]] = dp[i] + pmap[i]
            for j in range(i + dmap[i], n+2):
                if dp[j] < dp[i] + pmap[i]:
                    dp[j] = dp[i] + pmap[i]

print(dp[n+1])
