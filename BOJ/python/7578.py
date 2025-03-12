import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

tree = [0]*(1<<20)
C = 1<<19


def connect(index):  # 선 연결하고 트리 업데이트
    global tree, C

    cur = C+index
    while cur >= 1:
        tree[cur] += 1
        cur = cur//2


def divsum(cur_index, cur_left, cur_right, goal_left): # 현재 선을 그음으로써 겹치는 선들의 수 (구간합) 가져오기
    global tree

    if cur_right < goal_left:
        return 0

    if goal_left <= cur_left:
        return tree[cur_index]

    mid = (cur_left + cur_right) // 2

    return divsum(2*cur_index, cur_left, mid, goal_left) + divsum(2*cur_index+1, mid+1, cur_right, goal_left)


b2index = {}
for i in range(n):
    b2index[b[i]] = i

ans = 0
for i in range(n):
    b_idx = b2index[a[i]]
    ans += divsum(1,0,C-1,b_idx+1)
    connect(b_idx)

print(ans)
