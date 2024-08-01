def solution(num, k): #e.g. (29183, 2)
    a=str(num) #'29183'
    for i in range(len(a)): #a의 길이만큼 range 만들
        if a[i]==str(k): #'2'=='2'
            return i+1 #컴퓨터셈은 0부터 시작해서
    return -1