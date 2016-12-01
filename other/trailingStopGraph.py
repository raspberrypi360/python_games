'''
Created on Feb 15, 2016

@author: ryan
'''
import pandas
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import datetime as dt
import matplotlib.pyplot as plt

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
                return newData["Date"][i], newData["Adj Close"][i], ts, buyPrice, maxPrice, dateIndex, i
            elif newData["Adj Close"][i] > maxPrice:
                ts = 0.75 * newData["Adj Close"][i]
                maxPrice = newData["Adj Close"][i]
        return None, None
if __name__ == "__main__":
    dateBuy = "1988-12-02"
    rcParams['figure.figsize'] = 15, 6
    dateparse = lambda dates: pandas.datetime.strptime(dates, '%Y-%m-%d')
    data = pandas.read_csv('FMCC.csv', parse_dates='Date', index_col='Date',date_parser=dateparse)
    date, price, trail, buyPrice, peak, dateIndex, index = ts("FMCC.csv", dateBuy)
    print("Date: ", date, ", Price: ", price, ", Peak: ", peak, ", Trailing Stop: ", trail, ", Buy Price: ", buyPrice)
    ts = data['Adj Close']
    ts.head(10)
    markers_on = [dateIndex, index]
    plt.plot(data.index, ts, "-go", markevery=markers_on)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.axhline(peak)
    plt.show()