n = int(input())
ans = ["***","* *","***"]
i = 3
while i < n:
    # 아래로 3배 확장
    ans = 3 * ans

    # 오른쪽으로 3배확장
    for row in range(i):
        ans[row] = 3 * ans[row]
    for row in range(i, 2*i):
        ans[row] = ans[row] + i * " " + ans[row]
    for row in range(2*i, 3*i):
        ans[row] = 3 * ans[row]

    # 다음단계
    i *= 3

res = ""
for a in ans:
    res += a + "\n"
print(res)