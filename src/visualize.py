# visualization of trading indicators
import data
import process

import matplotlib as mpl
import matplotlib.pyplot as plt


# plot parameters
plt.style.use('dark_background')

# create empty axis and figure
fig = plt.figure(figsize=(10,5))
ax,macd = fig.subplots(2,sharex=True)

# draw chart from data
ax = data.draw_chart(ax, data.sec_hist, 'white','#a4a4a4')
#ax = process.sma(15, ax, data.sec_hist, '#2a2a2a')
ax = process.ema(5, ax, data.sec_hist, '#6a6a6a')
macd = process.macd(macd, data.sec_hist, '#6a6a6a','#2a2a2a')

# plot grid
ax.grid(linestyle='-', linewidth=1, color='#2a2a2a', zorder=1)
macd.grid(linestyle='-', linewidth=1, color='#2a2a2a', zorder=-1)

# axis lable formatting
ax.set_xticks(list(data.sec_hist['bar'])[::5])
ax.set_xticklabels(list(data.sec_hist['Date'].dt.strftime('%m-%d'))[::5])
plt.xticks(rotation=90)

# print security information
print(data.sec_hist.head())

# save and display plot
plt.savefig('../macd.png')
plt.show()
