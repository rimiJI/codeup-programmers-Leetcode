def solution(emergency):
    n=sorted(emergency,reverse=True)
    return [n.index(i)+1 for i in emergency]

