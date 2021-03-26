def dfs(node):
    # 이미 해당 부분문제를 계산해둔 경우
    if dp[node]:
        return dp[node]

    # 메모이제이션 안된 경우
    for p in parent[node]:
        dp[node] = max(dp[node], dfs(p) + buildtime[node])

    return dp[node]


# 여기부터 메인 실행 부분
n = int(input())
parent = [[] for row in range(n+1)]
buildtime = [0]
dp = [0]*(n+1)
for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    # 단일건물 건설시간
    buildtime.append(tmp[0])

    # 루트노드인 경우
    if len(tmp) == 2:
        dp[i] = buildtime[i]
        continue

    # 루트노드 아닌경우 부모노드 기록
    for p in tmp[1:-1]:
        parent[i].append(p)

for i in range(1, n+1):
    print(dfs(i))
