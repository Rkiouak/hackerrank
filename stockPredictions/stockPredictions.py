#!/usr/bin/py
import numpy
import math

def printTransactions(m, k, d, name, owned, prices):
    targetPrices=[]
    pricesStd=[]
    for i in range(len(prices)):
        targetPrices.append(sum(prices[i])/float(len(prices[i])))
        pricesStd.append(numpy.std(prices[i]))
        
    toBuy = -1
    maxDiff = -1
    toSell=[]
    for i in range(len(targetPrices)):
        if targetPrices[i]>prices[i][4]:
            if maxDiff<targetPrices[i]-prices[i][4] and prices[i][4]<=m:
                maxDiff=targetPrices[i]-prices[i][4]
                toBuy=i
        if targetPrices[i]<(prices[i][4]-pricesStd[i]*.5) and owned[i]>0:
            toSell.append(i)
    transactionCount=len(toSell)+(1 if toBuy>0 else 0)
    print(transactionCount)
    for i in toSell:
        print(name[i].strip()+' SELL '+str(owned[i])+'\n')
    if toBuy>0:
        print(name[toBuy].strip()+' BUY '+str(math.floor(m/prices[toBuy][4])))
            
    
            
    
if __name__ == '__main__':
    m, k, d = [float(i) for i in input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])

    printTransactions(m, k, d, names, owned, prices)
