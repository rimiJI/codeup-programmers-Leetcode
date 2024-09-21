def solution(M, N):
    answer = (M-1)+(N-1)*M
    return answer


# 2*2=1 1  1
# 2*5=1 1111 1111
# 1*1=0
# 3*4=11 111 111 111
# 즉, (m-1) +  (n-1)*m