'''
Created on Feb 15, 2016

@author: ryan
'''
import pandas

def ts(data, date):
    data = pandas.read_csv(data)
    buyPrice = None
    for i in range(len(data)):
        if data["Date"][i] == date:
            buyPrice = data["Adj Close"][i]
            dateIndex = i
            break
    if buyPrice == None:
        raise NameError("Date is not in data")
    else:
        maxPrice = buyPrice
        ts = 0.75 * buyPrice
        newData = data[:dateIndex]
        for i in range(len(newData["Adj Close"])-1, 0, -1):
            if newData["Adj Close"][i] <= ts:
                return newData["Date"][i], newData["Adj Close"][i]
            elif newData["Adj Close"][i] > maxPrice:
                ts = 0.75 * newData["Adj Close"][i]
                maxPrice = newData["Adj Close"][i]
        return None, None
if __name__ == "__main__":
    date, price = ts("FMCC.csv", "2016-03-21")
    if date != None:
        print("Sell on ", date, " at $", price)
    else:
        print("Hold")