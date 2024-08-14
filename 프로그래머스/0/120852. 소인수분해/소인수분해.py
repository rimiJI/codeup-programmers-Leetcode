def solution(n):
    answer = []
    for i in range(2,n+1):
        if n%i==0:
            if i not in answer:
                answer.append(i)
            while n%i==0:
                n//=i
    if n>1:
        answer.append(n)
    return answer