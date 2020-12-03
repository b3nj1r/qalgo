# visualization of trading indicators
import data
import process

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv') 

# retrieve close historical data 
df['Close'][:50].plot()
# plot last 5 close points from .csv data
plt.savefig('out.png')
plt.show()
