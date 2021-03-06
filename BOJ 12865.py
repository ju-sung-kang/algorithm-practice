import sys

n, k = map(int, sys.stdin.readline().split())
w = [0]  # 물건들 무게와 가치 저장
v = [0]
dp = [[0]*(k+1) for things in range(n+1)]

for i in range(n):
    weight, value = map(int, sys.stdin.readline().split())
    w.append(weight)
    v.append(value)

for i in range(1,n+1):
    for j in range(1,k+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k])