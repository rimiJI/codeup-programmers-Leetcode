def solution(money): 
    count = int(money/5500)
    left=int(money%5500)
    return [count,left]

#아메리카노 한잔에 5500, 갖은 돈 money -> 최대로 마실 수 있는 잔의 수와 남은 돈,,,,,,,
