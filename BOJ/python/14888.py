def dfs(step, res):                                                     # 나올 수 있는 모든 연산 결과 탐색
    global n                                                            # 재귀호출이 n-1번 수행되면(첫 수행 제외)
    global min_val                                                      # 재귀호출 한번당 연산 한번을 진행하므로
    global max_val                                                      # 연산이 종료되고 연산결과로 min max 업데이트
    global op

    if step == n-1:                                                     # dfs함수가 n번 수행되었음
        if res < min_val:
            min_val = res
        if res > max_val:
            max_val = res

    else:                                                               # 아직 중간단계라면
        if op[0] > 0:                                                     # + 연산 수행가능
            op[0] -= 1                                                      # + 연산 수행가능 횟수 -1
            dfs(step + 1, res + a[step + 1])                                # + 연산 수행
            op[0] += 1                                                      # 다른 루트의 연산에 영향을 주지 않기 위해 +1로 복구
        if op[1] > 0:                                                     # - 연산 수행가능
            op[1] -= 1
            dfs(step + 1, res - a[step + 1])
            op[1] += 1
        if op[2] > 0:                                                     # *(곱셈) 수행가능
            op[2] -= 1
            dfs(step + 1, res * a[step + 1])
            op[2] += 1
        if op[3] > 0:                                                     # /(나눗셈) 수행가능
            op[3] -= 1
            if res >= 0:                                                  # 나눗셈의 경우 문제의 지시대로 수행해야함
                dfs(step + 1, res // a[step + 1])
            else:  # res < 0
                dfs(step + 1, ((res * (-1)) // a[step + 1]) * (-1))
            op[3] += 1


# main
n = int(input())
a = list(map(int, input().split()))                                     # 피연산자 (숫자들) 저장하는 배열
op = list(map(int, input().split()))                                    # 연산자 (+ - * /) 저장하는 배열

min_val = pow(10, 9) + 1
max_val = min_val * (-1)

dfs(0, a[0])                                                            # 재귀호출 시작 (모든 연산루트 탐색)

print(max_val)
print(min_val)
