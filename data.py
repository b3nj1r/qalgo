# handle and manage historical data

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib as mpl

# get security history
sec = yf.Ticker('TSLA')
sec_hist = sec.history(period='120d')
sec_hist.reset_index(inplace=True)

# get bars
origin = sec_hist['Date'][0]
sec_hist['bar'] = sec_hist['Date'].map(lambda bar: (bar-origin).days)

def candlestick(ax,data,pos,neg):
    """Read price information to create a candlestick, return the axis with the added candle stick."""
    if data['Close'] > data['Open']:
        color = pos
    else:
        color = neg
    # create wick 
    ax.plot([data['bar'],data['bar']],[data['Low'],data['High']], linewidth=1, color=color)

    # create body
    rect = mpl.patches.Rectangle((data['bar'] - 0.25, data['Open']), 0.5, (data['Close'] - data['Open']), facecolor=color, edgecolor='none', linewidth=0, zorder=3)
    
    # add rectangle to axis
    ax.add_patch(rect)
    return ax

def draw_chart(ax, data, pos='white', neg='black'):
    """Iterate through data points, return axis with all added candlesticks"""
    for bar in range(data.shape[0]):
        ax = candlestick(ax,data.iloc[bar],pos,neg)
    return ax


