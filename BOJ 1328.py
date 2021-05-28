n, l, r = map(int, input().split())

dp = [[[0]*(r+1) for div2 in range(l+1)] for div1 in range(n+1)]

dp[1][1][1] = 1

for b in range(2,n+1):
    for lv in range(1,l+1):
        for rv in range(1,r+1):
            dp[b][lv][rv] = (dp[b-1][lv][rv] * (b-2) + dp[b-1][lv-1][rv] + dp[b-1][lv][rv-1]) % 1000000007

print(dp[n][l][r])