def solution(phone_book):
    hashdic={}
    
    for i in phone_book:
        hashdic[i]=True
        
    for i in phone_book:
        temp=""
        for n in i[:-1:]:
            temp+=n
            if temp in hashdic:
                return False   
    return True

