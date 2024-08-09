def solution(before, after):
    return 1 if ''.join(sorted(before,reverse=True)) ==''.join(sorted(after,reverse=True)) else 0
#만약 -1로 정렬 == after return1
#아니면 retrun 0