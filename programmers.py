#day1 두수의 곱
def solution(num1, num2):
    answer = 0
    if 0 <= num1 <= 100 and 0 <= num2 <= 100:
        answer=int(num1)*int(num2)
        return answer
