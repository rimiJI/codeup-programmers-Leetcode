def solution(s):
    stack=[]
    for i in s:
        if i =='(':
            stack.append(i)
        elif i ==')':
            if not stack:
                return False
            stack.pop()
    return len(stack)==0
    