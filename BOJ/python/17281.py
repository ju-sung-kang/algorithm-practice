from itertools import permutations


def score(hit_order):
    global max_score
    idx = 0
    score = 0
    for j in range(n):
        base, out = 0, 0
        while True:
            if pre_input[j][hit_order[idx]] == 0:  # 아웃!
                out += 1
                if out >= 3:
                    idx = (idx + 1) % 9
                    break
            elif pre_input[j][hit_order[idx]] == 1:  # 1루타!
                if base & (1 << 2): score += 1
                base = base<<1 | 1
            elif pre_input[j][hit_order[idx]] == 2:  # 2루타!
                if base & (1 << 2): score += 1
                if base & (1 << 1): score += 1
                base = base<<2 | 1<<1
            elif pre_input[j][hit_order[idx]] == 3:  # 3루타!
                if base & (1 << 2): score += 1
                if base & (1 << 1): score += 1
                if base & 1: score += 1
                base = (1 << 2)
            else:  # pre_input[j][hit_order[idx]] == 4  > 홈런!
                if base & (1 << 2): score += 1
                if base & (1 << 1): score += 1
                if base & 1: score += 1
                score += 1
                base = 0
            idx = (idx+1) % 9

    if score > max_score:
        max_score = score


n = int(input())
pre_input = []
for i in range(n):
    pre_input.append(list(map(int, input().split())))

permute = permutations(range(1,9), 8)
max_score = 0
for p in permute:
    tmp = list(p)
    tmp.insert(3,0)
    score(tmp)

print(max_score)
