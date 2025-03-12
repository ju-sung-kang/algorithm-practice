import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
mod = 1000000007
if arr[0] != 0 and arr[0] != -1:
    print(0)
else:
    dp = [0] * (n // 2 + 2)
    dp[0] = 1
    for r in range(1, n):
        tmp = [0] * (n // 2 + 2)
        if arr[r] == -1:
            if r < n / 2:
                for c in range(r + 1):
                    if c == 0:
                        tmp[c] += (dp[c] + dp[c + 1]) % mod
                    else:
                        tmp[c] += (dp[c - 1] + dp[c] + dp[c + 1]) % mod
            else:
                for c in range(n - r):
                    if c == 0:
                        tmp[c] += (dp[c] + dp[c + 1]) % mod
                    else:
                        tmp[c] += (dp[c - 1] + dp[c] + dp[c + 1]) % mod
        else:
            if r < n / 2:
                if arr[r] <= r:
                    c = arr[r]
                    if c == 0:
                        tmp[c] += (dp[c] + dp[c + 1]) % mod
                    else:
                        tmp[c] += (dp[c - 1] + dp[c] + dp[c + 1]) % mod
                    if tmp[c] == 0:
                        dp[0] = 0
                        break
                else:
                    dp[0] = 0
                    break
            else:
                if arr[r] <= n - 1 - r:
                    c = arr[r]
                    if c == 0:
                        tmp[c] += (dp[c] + dp[c + 1]) % mod
                    else:
                        tmp[c] += (dp[c - 1] + dp[c] + dp[c + 1]) % mod
                    if tmp[c] == 0:
                        dp[0] = 0
                        break
                else:
                    dp[0] = 0
                    break
        dp = tmp[:]

    print(dp[0])
