def solution(genres, plays):
    dic = {}
    total_plays = {}
    result = []
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g in dic:
            dic[g].append((p, i))  
            total_plays[g] += p 
        else:
            dic[g] = [(p, i)]
            total_plays[g] = p
    
    
    for g in dic:
        dic[g].sort(key=lambda x: x[0], reverse=True)

    sorted_genres = sorted(total_plays, key=total_plays.get, reverse=True)

    for g in sorted_genres:
        result.extend([i for _, i in dic[g][:2]]) 
    return result

