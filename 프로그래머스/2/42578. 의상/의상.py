from collections import Counter

def solution(clothes):
    category = [b for a, b in clothes]
    category_counter = Counter(category)

    mul = 1
    for count in category_counter.values():
        mul *= (count + 1)
    
    return mul - 1
