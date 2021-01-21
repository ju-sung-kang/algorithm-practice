def define_steam(num, start, end, s):                              # s팀을 재귀적으로 정하고 다 정해졌으면 능력치 차이 계산
    global n                                                       # 그리고 차이중 최솟값을 min_val 에 저장
    global nd2
    global min_val

    if num == nd2:                                                 # 팀이 다 나누어진 경우
        stscore = 0
        ltscore = 0
        l = []
        for i in range(n):
            if i not in s:
                l.append(i)

        for j1 in range(nd2 - 1):                                    # 팀별 능력치 계산
            for j2 in range(j1+1, nd2):
                stscore += arr[s[j1]][s[j2]] + arr[s[j2]][s[j1]]
                ltscore += arr[l[j1]][l[j2]] + arr[l[j2]][l[j1]]

        if abs(stscore - ltscore) < min_val:                         # 능력치 차이 최솟값을 업데이트
            min_val = abs(stscore - ltscore)

    else:                                                          # 팀이 아직 안나누어진 경우
        for i in range(start, end):
            define_steam(num + 1, i + 1, end + 1, s + [i])


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

min_val = float("inf")
nd2 = n//2                                                         # 그냥 n//2를 자주 쓰니까 지저분해보여서 nd2로 바꿔서 저장

define_steam(1, 1, n-(nd2 - 2), [0])                               # 처음에 0을 s팀에 포함시킴, 0이 l팀에 있는 경우의 차이값은
print(min_val)                                                     # 0이 s팀에 있는 경우의 차이값과 중복되기 때문에
