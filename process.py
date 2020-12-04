# process prepared data using talib
# TODO: implement source code for algos
import numpy as np

def sma(window, ax, data, color):
    
    # create new collumn and fill it with the mean for the last 3 bars 
    
    data['sma'] = data.iloc[:,1].rolling(window=window).mean()
    # plot new data
    ax.plot(data['bar'],data['sma'],color=color)
    
    print(data.head())
    return ax
