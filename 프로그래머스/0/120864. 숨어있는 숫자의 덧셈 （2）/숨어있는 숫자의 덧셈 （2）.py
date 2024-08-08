def solution(my_string):
    answer = 0
    num_str=''
    for i in my_string:
        if i.isdigit():
            num_str+=i
        else:
            num_str+=' '
            
    num_list=map(int,num_str.split())
    
    return sum(num_list)