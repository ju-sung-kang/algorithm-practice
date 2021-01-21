n, l = map(int, input().split())
rmap = []
for i in range(n):
    rmap.append(list(map(int, input().split())))

ans = 0  # 건널수 있는 길의 수
# row들 검사
for i in range(n):
    prev = rmap[i][0]                                   # prev는 전 블록의 높이 저장
    cnt = -1                                            # cnt는 평지가 얼마나 지속됐는지를 저장 (평지 지속 후 올라갈때만 적용)
    j = 0
    while j < n:
        if prev != rmap[i][j]:                          # 올라가거나 내려가게 됨
            if prev - rmap[i][j] == -1:                     # 올라가게 된 경우
                if cnt < l-1:
                    break
                else:
                    cnt = 0
            elif prev - rmap[i][j] == 1:                    # 내려가게 된 경우
                if j + l > n:                                   # 남은 길의 길이가 경사로 놓기에 부족한 경우 탐색 끝냄
                    break
                else:                                           # 그렇지 않다면
                    can = True
                    for k in range(1, l):                           # 경사로를 놓을만큼의 평지가 확보되어있는지 검사
                        if rmap[i][j] != rmap[i][j+k]:
                            can = False
                            break
                    if can:                                         # 확보되어있다면 경사로 길이만큼 검사를 건너뛴다
                        j += l-1
                        cnt = -1                                        # 평지지속 카운트 업데이트
                    else:
                        break
            elif abs(prev - rmap[i][j]) >= 2:           # 차이가 1이아니면 경사로를 놓을 수없음
                break

        else:                                           # 평지 지속
            cnt += 1

        if j == n-1:                                    # 길의 끝에 도달했다면
            ans += 1
            break
        else:                                           # 아니라면 prev업데이트
            prev = rmap[i][j]
            j += 1

# col들 검사 row 검사와 방식은 동일하다
for i in range(n):
    prev = rmap[0][i]
    cnt = -1
    j = 0
    while j < n:
        if prev != rmap[j][i]:
            if prev - rmap[j][i] == -1:
                if cnt < l-1:
                    break
                else:
                    cnt = 0
            elif prev - rmap[j][i] == 1:
                if j + l > n:
                    break
                else:
                    can = True
                    for k in range(1, l):
                        if rmap[j][i] != rmap[j+k][i]:
                            can = False
                            break
                    if can:
                        j += l - 1
                        cnt = -1
                    else:
                        break
            elif abs(prev - rmap[j][i]) >= 2:
                break

        else:
            cnt += 1

        if j == n - 1:
            ans += 1
            break
        else:
            prev = rmap[j][i]
            j += 1

print(ans)
