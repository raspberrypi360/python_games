'''
Created on Feb 15, 2016

@author: ryan
'''
def stockProblem(prices):
    high = None
    low = None
    newLow = None
    for i, price in enumerate(prices):
        if i == 0:
            newLow = price
        else:
            if high == None:
                if price > newLow:
                    high = price
                    low = newLow
                    newLow = None
                elif price < newLow:
                    newLow = price
            else:
                if newLow == None:
                    if high < price:
                        high = price
                    elif price < low:
                        newLow = price
                else:
                    if high < price:
                        high = price
                        low = newLow
                        newLow = None
                    elif low > price:
                        if price < newLow:
                            newLow = price
                    elif price < high and price > low:
                        if (price - newLow) > (high - low):
                            high = price
                            low = newLow
                            newLow = None
    if high == None:
        return [None, None, 0]
    return [high, low, (high - low)]

if __name__ == "__main__":
    prices = [5, 7, 1, 9, 2, 16, 3]
    high, low, profit = stockProblem(prices)
    print(high, low, profit)