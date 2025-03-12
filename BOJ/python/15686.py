from itertools import combinations


def distance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


def chickenDistance(clist, pos):
    mind = float("inf")
    for c in clist:
        if distance(c, pos) < mind:
            mind = distance(c,pos)

    return mind


n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

home = []
chicken = []

for r in range(n):
    for c in range(n):
        if city[r][c] == 1:
            home.append((r,c))
        elif city[r][c] == 2:
            chicken.append((r,c))


if len(chicken) <= m:
    ans = 0
    for h in home:
        ans += chickenDistance(chicken, h)
    print(ans)

else:  # 치킨집이 m개보다 많음
    min_val = float('inf')
    for ctuple in combinations(chicken, m):
        ans = 0
        for h in home:
            ans += chickenDistance(list(ctuple), h)
        if ans < min_val:
            min_val = ans
    print(min_val)