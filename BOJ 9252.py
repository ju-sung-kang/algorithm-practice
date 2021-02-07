s1 = input()
s2 = input()

n1 = len(s1)
n2 = len(s2)

dp = [[0]*n2 for row in range(n1)]

for i in range(n1):
    for j in range(n2):
        if s1[i] == s2[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
        else:
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

row = n1-1
col = n2-1
ans = ""
if dp[row][col] == 0:
    print(0)
else:
    while True:
        if s1[row] == s2[col]:
            ans = s1[row] + ans
            if dp[row][col] <= 1:
                break
            else:
                row -= 1
                col -= 1
        else:
            if row == 0:
                col -= 1
            elif col == 0:
                row -= 1
            else:
                if dp[row-1][col] >= dp[row][col-1]:
                    row -= 1
                else:
                    col -= 1
    print(len(ans))
    print(ans)