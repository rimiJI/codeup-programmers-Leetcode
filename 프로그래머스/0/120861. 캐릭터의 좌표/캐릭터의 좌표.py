def solution(keyinput, board):
    w,h=[0,0]
    w2,h2=board
    for i in keyinput:
        if i=="right" and w < w2//2 :
            w+=1
        elif i =="left" and w > -(w2//2):
            w-=1
        elif i =="up" and h < h2//2:
            h+=1
        elif i=="down"and h > -(h2//2) :
            h-=1
    
    return [w,h]