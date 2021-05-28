from collections import deque

n, w, l = map(int, input().split())
t = list(map(int,input().split()))
t = deque(t)
b = deque([0]*w)
time = 0
while t or sum(b) > 0:
    b.popleft()

    if t:
        if sum(b) + t[0] <= l:
            b.append(t.popleft())
        else:
            b.append(0)

    time += 1

print(time)