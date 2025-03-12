n=int(input())
dp=[None]*(n+1)
dp[1] = 0
for i in range(2,n+1):
    prev_steps = [dp[i-1]]
    if i%3==0 and i//3>=1:
        prev_steps.append(dp[i//3])
    if i%2==0 and i//2>=1:
        prev_steps.append(dp[i//2])
    dp[i] = min(prev_steps)+1

print(dp[n])