from collections import deque

def solution(priorities, location):
    que = deque([(p,i) for i,p in enumerate(priorities)])
    
    answer=0
    
    while que:
        current = que.popleft()
        if any(current[0]<other[0] for other in que):
            que.append(current)
        else:
            answer += 1
            if current[1]==location:
                return answer