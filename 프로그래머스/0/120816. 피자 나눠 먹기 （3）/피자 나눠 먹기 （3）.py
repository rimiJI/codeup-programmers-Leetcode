def solution(slice, n):
    p=1
    while n > (slice*p):
        p+=1
    return p