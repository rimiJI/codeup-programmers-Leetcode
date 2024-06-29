def solution(array, n):
    count=0
    for i in array:
        if i==n:
            count+=1
    return count