import math

def mean(alist):
    mean = sum(alist) / len(alist)
    return mean

def standardDev(alist):
    theMean = mean(alist)    
    sum = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        sum = sum + diffsq
        
    sdev = math.sqrt(sum/(len(alist)-1))
    return sdev

def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd) 
    return corr

def stockCorrelate():
    url1 = open('aapl2.csv')
    url2 = open('amzn2.csv')
    t1Data = url1.readlines()
    t2Data = url2.readlines()  
  
    t1Data = [line[0:-1].split(',') for line in t1Data[1:] ] 
    # list of rows as lists, i.e. one row is a list of strings
    # print('list of two lists', t1Data[0:2])
    t2Data = [line[0:-1].split(',') for line in t2Data[1:] ]  
    
    t1Close = []
    t2Close = []
    for i in range(min(len(t1Data), len(t2Data))):   
        if t1Data[i][0] == t2Data[i][0]:
            t1Close.append(float(t1Data[i][4]))#share price, at opening or closing?
            t2Close.append(float(t2Data[i][4]))   

    return correlation(t1Close, t2Close)


import turtle

def plotPts(): 
#   # add your code here to plot the data

    url1 = open('aapl2.csv')
    url2 = open('amzn2.csv')
    t1Data = url1.readlines()
    t2Data = url2.readlines()  
  
    t1Data = [line[0:-1].split(',') for line in t1Data[1:] ] 
    # list of rows as lists, i.e. one row is a list of strings
    # print('list of two lists', t1Data[0:2])
    t2Data = [line[0:-1].split(',') for line in t2Data[1:] ]  
    
    t1Close = []
    t2Close = []
    for i in range(min(len(t1Data), len(t2Data))):   
        if t1Data[i][0] == t2Data[i][0]:
            t1Close.append(float(t1Data[i][4]))#share price, at opening or closing?
            t2Close.append(float(t2Data[i][4]))
             
    drawPlot= turtle.Scren()
    drawPlot.setworldcoordinates(100,100, 1200, 1200)
    t =turtle.Turtle()
    print( t1Close[0:8])
    print(len(t1Close))
    for i in range(1, len(t1Close)):
        t.up()
        t.goto(t1Close[i], t2Close[i])
        t.down()
        t.dot()
    drawPlot.exitonclick()
    turtle.done()
    
    
                
# main program starts here
corrResult = stockCorrelate()
print( corrResult)

