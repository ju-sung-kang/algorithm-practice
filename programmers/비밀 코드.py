from collections import deque

def compare(_target, _candidate):
    target = deque(_target)
    candidate = deque(_candidate)
    cnt = 0
    cur = target[0] if target[0] < candidate[0] else candidate[0]
    while len(target) > 0 and len(candidate) > 0:
        if target[0] == candidate[0]:
            target.popleft()
            candidate.popleft()
            
            cnt += 1
        elif target[0] <= cur:
            target.popleft()
        elif candidate[0] <= cur:
            candidate.popleft()

        if len(target) == 0 or len(candidate) == 0: break
        
        cur = min(target[0], candidate[0])
    return cnt
            
        

def solution(n, q, ans):
    # 시도들이 주어지고, 그 시도마다 몇개를 맞혔는지 알려줌
    # 그럼 내가 최종적으로 구해야하는건 이 시나리오에서 가능한 정답조합이 몇개인지
    # 참고로 수열의 길이는 5로 고정임
    # brute force?
    
    
    # 가능한 모든 비밀코드를 탐색
    cnt = 0 
    for a1 in range(1,n-3):
        for a2 in range(a1+1,n-2):
            for a3 in range(a2+1, n-1):
                for a4 in range(a3+1, n):
                    for a5 in range(a4+1, n+1):
                        valid = True
                        for i in range(len(q)):
                            candidate, answer = q[i], ans[i]
                            #print('candidate', candidate, 'answer', answer, 'q', q, 'ans', ans)
                            if compare([a1,a2,a3,a4,a5], candidate) != ans[i]: valid=False
                        if valid: cnt += 1
                    
                            
                                
                    
    answer = 0
    return cnt


print(solution(15,	[[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]],	[2, 1, 3, 0, 1]))