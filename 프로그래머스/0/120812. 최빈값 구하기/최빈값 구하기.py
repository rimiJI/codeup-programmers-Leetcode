from collections import Counter

def solution(array):
    count = Counter(array)
    max_c= max(count.values())
    most_c=[num for num,fr in count.items() if fr==max_c]

    if len(most_c)>1:
        return -1
        
    return most_c[0]