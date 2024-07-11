def solution(hp):
    count=0
    a,b,c=5,3,1
    
    while hp!=0:
        if hp>=5:
            hp-=5
            count+=1
        elif 3<=hp<5:
            hp-=3
            count+=1
        elif 1<=hp<3:
            hp-=1
            count+=1

    return count