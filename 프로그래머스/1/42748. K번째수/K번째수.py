def solution(array, commands):
    answer=[]
    for c in commands:
        i,j,k=c
        sli_arr=sorted(array[i-1:j])
        answer.append(sli_arr[k-1])
        
    return answer