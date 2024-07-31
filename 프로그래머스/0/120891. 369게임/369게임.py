def solution(order):
    order=str(order)
    a=0
    for i in order:
        if i=='3' or i=='6' or i=='9':
            a+=1
    return a