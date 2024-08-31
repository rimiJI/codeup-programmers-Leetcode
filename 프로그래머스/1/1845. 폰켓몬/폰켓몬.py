def solution(nums):
    if len(list(set(nums))) > len(nums)/2:
        return len(nums)/2
    else:
        return len(list(set(nums)))
