import sys

n = int(sys.stdin.readline())

# 배열선언
arr = [[float("inf")]*n for row in range(n)]
for d in range(n):
    arr[d][d] = 0

# 인접행렬 입력받기
m = int(input())
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)

# 플로이드 와샬 알고리즘
for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

# 출력
for i in range(n):
    for j in range(n):
        sys.stdout.write(str(arr[i][j]) + " ") if arr[i][j] != float("inf") else sys.stdout.write("0 ")
    sys.stdout.write("\n")