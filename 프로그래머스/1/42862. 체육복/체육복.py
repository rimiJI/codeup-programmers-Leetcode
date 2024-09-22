def solution(n, lost, reserve):

    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)
    
    return n - len(lost_set)


# 12345-24=135+135=113355=12345=5
# 12345-24=135+3=1335=1345=4
# 123-3=12+1=112=2

# for i in range(n):
#     a+=i