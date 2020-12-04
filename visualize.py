# visualization of trading indicators
import data
import process

import matplotlib as mpl
import matplotlib.pyplot as plt


# plot parameters
mpl.rcParams['axes.facecolor'] = '#2a2a2a'

# create empty axis and figure
fig = plt.figure(figsize=(10,5),facecolor='white')
ax = fig.add_subplot(111)

# draw chart from data
ax = data.draw_chart(ax, data.sec_hist, 'green','red')
ax = process.sma(15, ax, data.sec_hist, 'yellow')
ax = process.sma(5, ax, data.sec_hist, 'white')
# plot grid
ax.grid(linestyle='-', linewidth=1, color='#4a4a4a', zorder=1)

# axis lable formatting
ax.set_xticks(list(data.sec_hist['bar'])[::5])
ax.set_xticklabels(list(data.sec_hist['Date'].dt.strftime('%m-%d'))[::5])
plt.xticks(rotation=90)

# print security information
print(data.sec_hist.head())

# save and display plot
plt.savefig('sma.png')
plt.show()
