def solution(rsp):
    a=""
    for i in rsp:
        if i=="0":
            a+="5"
        elif i=="2":
            a+="0"
        elif i=="5":
            a+="2"
    return a
            