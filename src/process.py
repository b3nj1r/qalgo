# process prepared data using talib
import numpy as np
import talib as ta


def sma(window, ax, data, color):

    # create new collumn and fill it with the mean for the l
    data['sma'] = data.iloc[:,1].rolling(window=window).mean()
    # plot new data
    ax.plot(data['bar'],data['sma'],color=color)

    print(data.head())
    return ax

def ema(k,ax,data,color):
    data['ema'] = ta.EMA(data['Close'],k)
    ax.plot(data['bar'],data['ema'],color=color)
    return ax

def macd(ax,data,bright,dark):
    data['macd'],data['macdsignal'],data['macdhist'] = ta.MACD(data['Close'],12,26,9)
    ax.plot(data['bar'],data['macd'],color=bright)
    ax.plot(data['bar'],data['macdsignal'],color=dark)
    ax.bar(data['bar'],data['macdhist'],color=[bright,dark])
    return ax
