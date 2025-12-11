import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
df["Return"] = df["Close"].pct_change()

# 3.1 Rolling mean (moving average)

df["MA_3"] = df["Close"].rolling(window=3).mean()

''' 
rolling(window=3) creates a rolling view over 3 rows; .mean() computes the average in each window.​
''' 

# 3.2 Rolling volatility (std of returns)

df["Vol_5"] = df["Return"].rolling(window=5).std()

'''
This approximates 5-day rolling volatility, a common risk metric.
'''

# 4. Plot price + moving average

plt.figure(figsize=(8,4))
df["Close"].plot(label="Close")
df["MA_3"].plot(label="MA_3", linestyle = "--")
plt.legend()
plt.title("Close price and 3-day moving average")
plt.grid(True)
plt.show()