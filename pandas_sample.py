import pandas as pd
import datetime
from pandas_datareader import data, wb

import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 9, 1)

df = data.DataReader("XOM", "yahoo", start, end)

print(df)

print(df.head())

gdp = data.DataReader("GDP", "fred", start, end)

print(gdp)

style.use('fivethirtyeight')

df['High'].plot()
plt.legend()
plt.show()