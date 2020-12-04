# process prepared data using talib
# TODO: implement source code for algos
import numpy as np

def sma(ax, data, color):
    #plt.plot([x1,x2], [y1,y2])
    #ax.plot([data['bar']],[data['Close'].mean()], linewidth=10, color=color)
    data['sma3'] = data.iloc[:,1].rolling(window=3).mean()
    print(data.head())
    ax.plot(data['bar'],data['sma3'])
    return ax
