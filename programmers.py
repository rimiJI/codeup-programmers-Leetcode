# #day1 두수의 곱
# def solution(num1, num2):
#     answer = 0
#     if 0 <= num1 <= 100 and 0 <= num2 <= 100:
#         answer=int(num1)*int(num2)
#         return answer


# def solution(n):
#     if n<=7:
#         return 1
#     else:
#         return (n//7)+1
    

# n=int(input())
# print(solution(n))



# def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
#     if square_target < 0:
#         raise ValueError('Square root of negative number is not defined in real numbers')
#     if square_target == 1:
#         root = 1
#         print(f'The square root of {square_target} is 1')
#     elif square_target == 0:
#         root = 0
#         print(f'The square root of {square_target} is 0')
#     else:
#         low=0
#         high=max(1,square_target)


#n인분 , 음료수 k개 총얼마지불?? 양꼬치 1인분 12000 , 음료수 2000 .10인분먹으면 음료수 하나 서비스

# def solution(n,k):
#     return n*12000+k*2000-int(n/10)*2000

# n,k=map(int,input().split())
# print(solution(n,k))


# #문자열안에 문자열 
# def solution(str1, str2):
#     if str2 in str1:
#         return 1
#     else:
#         return 2
    
    
# str1,str2=input().split()
# print(solution(str1, str2))


