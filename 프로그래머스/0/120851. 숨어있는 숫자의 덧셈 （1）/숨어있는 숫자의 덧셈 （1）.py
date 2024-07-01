def solution(my_string):
    answer=0
    
    for c in my_string:
        if c.isdigit():#문자 정수 유무
            answer += int(c)
    return answer