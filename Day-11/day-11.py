import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulating daily returns with NumPy

np.random.seed(42)  # for reproducibility
n_days = 252        # ~1 trading year

mu_daily = 0.0005   # 0.05% per day
sigma_daily = 0.01  # 1% daily volatility

returns_sim = np.random.normal(loc=mu_daily, scale=sigma_daily, size=n_days)
print("Mean:", returns_sim.mean(), "Std:", returns_sim.std())

# creating a price path
start_price = 100
prices_sim = start_price * (1 + returns_sim).cumprod()
dates = pd.date_range(start="2025-01-01", periods=n_days, freq="B")

df_sim = pd.DataFrame({"Price": prices_sim, "Return": returns_sim}, index=dates)
print(df_sim.head())

# 2. Quick EDA on simulated series

print(df_sim["Return"].describe())
print(df_sim["Price"].describe())

df_sim["Price"].plot(figsize=(8,4), title = "Simulated price path")
plt.grid(True)
plt.show()

df_sim["Return"].hist(bins=30,figsize=(8,4))
plt.title("Simulated Dailyu Return Distribution")
plt.grid(True)
plt.show()

# 3. Resampling: daily → weekly / monthly

df = df_sim
weekly = df["Price"].resample("W").last()
monthly = df["Price"].resample("M").last()

print(weekly.head())
print(monthly.head())

# computing weekly returns 
weekly_ret = weekly.pct_change()
print(weekly_ret.describe())