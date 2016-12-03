'''
Created on Feb 15, 2016

@author: ryan
'''
from __future__ import division
import pandas
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import datetime as dt
import matplotlib.pyplot as plt

def rsiCompute(data, numPeriods):
    n = len(data)
    price = data["Close"].tolist()
    rsi = [None for i in range(n)]
    startPrices = price[:numPeriods]
    gain = 0
    loss = 0
    for i in range(numPeriods-1):
        if startPrices[i+1]>startPrices[i]:
            gain += startPrices[i+1]-startPrices[i]
        else:
            loss += startPrices[i]-startPrices[i+1]
    avgGain = gain/numPeriods
    avgLoss = loss/numPeriods
    for i in range(numPeriods, n):
        if i>numPeriods:
            p1 = price[i]
            p2 = price[i-1]
            if p1>p2:
                gain = p1-p2
                loss = 0
            else:
                loss = p2-p1
                gain = 0
            avgGain = (avgGain*(numPeriods-1)+gain)/numPeriods
            avgLoss = (avgLoss*(numPeriods-1)+loss)/numPeriods
        if avgLoss == 0:
            rs[i] = 100
        else:
            rs = avgGain/avgLoss
            rsi[i] = 100-100/(1+rs)
    data["rsi"]  = rsi

def buyOrSell(dataWithInd, overBought, overSold):
    n = len(dataWithInd)
    res = ['-' for i in range(n)]
    rsi = dataWithInd["rsi"].tolist()
    for i in range(n):
        if rsi[i] <= overBought:
            if i==0:
                res[i] = 'B'
            elif rsi[i-1]>overBought:
                res[i] = 'B'
        elif rsi[i] >= overSold:
            if i==0:
                res[i] = 'S'
            elif rsi[i-1]<overSold:
                res[i] = 'S'
    dataWithInd['bs'] = res

def computeProfit(dataList, symbols, totalPortfolio, tradeSize, tradeFee, buyOnly=True):
    numTrades = 0
    totalProfit = 0
    portCost = 0
    portShares = 0
    numSells = 0
    numBuys = 0
    cashAvail = totalPortfolio
    n = len(dataList[0])
    bss = [dataList[i]['bs'].tolist() for i, sym in enumerate(symbols)]
    prices = [dataList[i]["Adj Close"].tolist() for i, sym in enumerate(symbols)]
    for i in range(n):
        for j, sym in enumerate(symbols):
            bs = bss[j]
            price = prices[j][i]
            if bs[i] == 'B':
                shares = int(tradeSize/price)
                if shares>0 and cashAvail >= shares*price + 2*tradeFee:
                    portShares += shares
                    cost = shares*price + tradeFee
                    portCost += cost
                    cashAvail -= cost
                    numBuys += 1
            elif (not buyOnly and bs[i] == 'S') or i==n-1:
                if portShares>0:
                    portCost += tradeFee
                    cashAvail += portShares*price-tradeFee    
                    portShares = 0
                    numSells += 1
    totalProfit = cashAvail - totalPortfolio
    numTrades = numBuys + numSells
    return totalProfit, numTrades, numBuys, numSells        
    
def testData(symbols, periods, low, high, portfolio, tradeSize, tradeFee, firstOnly=0, reverse=True, buyOnly=True, plot=False):     
    numSym = len(symbols)
    ress = [[] for sym in symbols]
    for i, sym in enumerate(symbols):
        data = pandas.read_csv(sym+".csv")
        if reverse:
            data = data[::-1]
        if firstOnly>0:
            res = data[:firstOnly].copy()
        else:
            res = data.copy()
        ress[i] = res
        rsiCompute(res, periods)
        buyOrSell(res, low, high)
    tp, nt, nb, ns = computeProfit(ress, symbols, portfolio, tradeSize, tradeFee, buyOnly)
    print("tp = ",tp,", nt = ",nt,", nb = ",nb,", ns = ",ns)
    print("profit % = ", tp/portfolio*100)

#     print(res['rsi'])
    if plot and numSym == 1:
        res = ress[0]
        n = len(res)
        rcParams['figure.figsize'] = 60, 12
        bs = np.array(res['bs'])
        x = np.arange(n)
        markers_onB = x[bs=='B']
        markers_onS = x[bs=='S']
        plt.plot(x, res["Adj Close"], '-bo', label='spy', markevery=markers_onB)
        plt.plot(x, res["rsi"], '-ro', label='RSI', markevery=markers_onS)
        plt.axhline(low)
        plt.axhline(high)
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.show()

       
if __name__ == "__main__":
#     testData('test.csv', 14, 30, 70, 10000, 200, 7, 0, False)
#    testData(["r"], 21, 40, 75, 100000, 2000, 7.95, 0, True, False, False)
    testData(["r", "x", "hon", "d", "bll", "cat", "ge", "k"], 21, 40, 80, 100000, 2000, 7.95, 0, True, False, False)
 