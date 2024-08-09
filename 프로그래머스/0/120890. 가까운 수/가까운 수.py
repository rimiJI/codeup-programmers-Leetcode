def solution(array, n):
    ar_abs=[(abs(n-i),i) for i in array]
    ar_abs.sort()
    return ar_abs[0][1]