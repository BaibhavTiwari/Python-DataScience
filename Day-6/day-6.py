import  pandas as pd 
import matplotlib.pyplot as plt

# 1. Setup and load data

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
print(df.head())

#2. Plot price time series

plt.figure(figsize = (8,4))
df["Close"].plot()
plt.title("Closing price over time")
plt.xlabel("Date")
plt.ylabel("price")
plt.grid(True)
plt.show()

# DataFrame.plot() uses Matplotlib under the hood to create a line plot, ideal for stock series.​

# Grid, labels, and title make it readable like a basic trading chart.

# 3. Compute and plot returns distribution

df["Return"] = df["Close"].pct_change()
print(df["Return"].describe())

plt.figure(figsize=(8,4))
df["Return"].hist(bins=20)
plt.title("daily return distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()