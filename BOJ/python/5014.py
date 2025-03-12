from collections import deque

F,S,G,U,D=map(int, input().split())

ans = "use the stairs"
visit=[False]*(F+1)
q=deque([(S,0)])
visit[S]=True
while q:
    cur_floor, button_click = q.popleft()
    if cur_floor==G:
        ans=button_click
        break
    else:
        if cur_floor-D>=1 and not visit[cur_floor-D]:
            q.append((cur_floor-D, button_click+1))
            visit[cur_floor-D]=True
        if cur_floor+U<=F and not visit[cur_floor+U]:
            q.append((cur_floor+U, button_click+1))
            visit[cur_floor+U]=True

print(ans)