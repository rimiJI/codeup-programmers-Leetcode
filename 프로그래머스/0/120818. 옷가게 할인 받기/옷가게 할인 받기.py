def solution(price):
    if price < 100000:
        return int(price)
        
    elif 100000<= price<300000 :
        return int(price - price/100*5)
    
    elif 300000<= price<500000 :
        return int(price - price/100*10)
    
    else:
        return int(price -price/100*20)