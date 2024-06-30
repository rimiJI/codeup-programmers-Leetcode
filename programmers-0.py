#문자열안에 문자열 
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
    
str1,str2=input().split()
print(solution(str1, str2))