from collections import deque
from itertools import combinations

def convert(s):
    return int(s)-1

n = int(input())
people = list(map(int,input().split()))
adj = []
for i in range(n):
    tmp = list(map(convert,input().split()))
    adj.append(tmp[1:])

ans = 1000
for redteamnum in range(1,n//2+1):
    for redteam in combinations(list(range(n)), redteamnum):
        blueteam = []
        for b in range(n):
            if b not in redteam:
                blueteam.append(b)
        flag = True

        q = deque()
        check = [False]*n
        q.append(redteam[0])
        check[redteam[0]] = True
        tmp = [redteam[0]]
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if not check[nxt] and nxt in redteam:
                    check[nxt] = True
                    q.append(nxt)
                    tmp.append(nxt)
        if set(tmp) != set(redteam):
            flag = False

        q = deque()
        check = [False] * n
        q.append(blueteam[0])
        check[blueteam[0]] = True
        tmp = [blueteam[0]]
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if not check[nxt] and nxt in blueteam:
                    check[nxt] = True
                    q.append(nxt)
                    tmp.append(nxt)
        if set(tmp) != set(blueteam):
            flag = False

        if flag:
            redtotal = 0
            for r in redteam:
                redtotal += people[r]
            if ans > abs(sum(people) - redtotal - redtotal):
                ans = abs(sum(people) - redtotal - redtotal)


if ans == 1000:
    print(-1)
else:
    print(ans)