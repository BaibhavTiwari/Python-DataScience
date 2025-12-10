import pandas as pd
import matplotlib.pyplot as plt

# 1. Setup and load data
df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
print(df.head())

# 2. Plot price time series
plt.figure(figsize=(8, 4))
df["Close"].plot()
plt.title("Closing price over time")
plt.xlabel("Date")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# 3. Compute and plot returns distribution
df["Return"] = df["Close"].pct_change()
print(df["Return"].describe())

plt.figure(figsize=(8, 4))
df["Return"].hist(bins=20)
plt.title("Daily return distribution")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 4. Class counts bar chart (Return_Class)

def classify_return(r):
    if pd.isna(r):
        return "No data"
    if r > 0.02:
        return "Strong up"
    elif r > 0:
        return "Mild up"
    elif r > -0.02:
        return "Mild down"
    else:
        return "Strong down"

df["Return_Class"] = df["Return"].apply(classify_return)

return_counts = df["Return_Class"].value_counts()

plt.figure(figsize=(6, 4))  # fixed: plt, not plty
return_counts.plot(kind="bar")
plt.title("Count of return classes")
plt.xlabel("Class")
plt.ylabel("Count")
plt.grid(axis="y")
plt.show()
