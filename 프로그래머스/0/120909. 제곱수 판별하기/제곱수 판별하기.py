def solution(n):
    if n%(n**(1/2))==0:
        return 1
    else:
        return 2