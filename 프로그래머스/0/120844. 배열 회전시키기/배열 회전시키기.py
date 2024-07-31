def solution(numbers, direction):
    a=numbers
    if direction=='right':
        a.insert(0,a[-1]) 
        a.pop()
    else:
        a.append(a[0])
        a=a[1:]
        
    return a


