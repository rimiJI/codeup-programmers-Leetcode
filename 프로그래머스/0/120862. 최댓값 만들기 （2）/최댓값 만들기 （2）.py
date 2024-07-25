def solution(numbers):
    a = sorted(numbers,reverse=True)
    return max ( a[0]*a[1] , a[-1]*a[-2] )