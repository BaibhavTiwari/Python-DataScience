import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simulate many price paths

np.random.seed(42)

n_days = 252          
n_paths = 500         
mu_daily = 0.0005   
sigma_daily = 0.01   

# shape: (n_days, n_paths)
returns = np.random.normal(loc=mu_daily, scale=sigma_daily, size=(n_days, n_paths))

start_price = 100
prices = start_price * (1 + returns).cumprod(axis=0)

dates = pd.date_range(start="2025-01-01", periods=n_days, freq="B")
df_prices = pd.DataFrame(prices, index=dates)

# 2. Look at final outcomes distribution

final_prices = df_prices.iloc[-1, :]
print(final_prices.describe())

final_prices.hist(bins=30, figsize=(8,4))
plt.title("Distribution of final prices(500 paths)")
plt.xlabel("final price")
plt.ylabel("frequency")
plt.grid(True)
plt.show()

# 3. Probabilities of outcomes

prob_above_120 = (final_prices > 120).mean()
prob_below_80 = (final_prices < 80).mean()

print("P(Price > 120):", prob_above_120)
print("P(Prices < 80):",prob_below_80)