def solution(i, j, k):
    num_str=''.join([str(a) for a in range(i,j+1) ])
    num_list=list(num_str)
    return num_list.count(str(k))
