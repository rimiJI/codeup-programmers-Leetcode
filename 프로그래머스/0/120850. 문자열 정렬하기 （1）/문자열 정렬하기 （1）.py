def solution(my_string):
    my_string=sorted(list(my_string))
    return [int(i) for i in my_string if i.isdigit() ]
 
    
#만약 i 가 int면 원소에 넣고 아니면 ''
#리스트로 만들어라