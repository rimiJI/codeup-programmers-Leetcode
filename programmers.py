#자동입력 int 

#int -> string -> [ for in ] -> sum


n=int(input())

def solution(n):
    return sum(map(int,[str(n)]))

print(solution(n))