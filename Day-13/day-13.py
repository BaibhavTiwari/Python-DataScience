import numpy as np
import pandas as pd 

np.random.seed(42)

n_days = 252
n_paths = 500

mu_daily = 0.005
sigma_daily  = 0.81

ret = np.random.normal(loc=mu_daily, scale=sigma_daily,size=(n_days, n_paths))

# 2. Apply a simple “strategy” on all paths
'''
Toy rule: reduce exposure when return is very negative (e.g., cut to 0.5 position if previous day return < −2%).
'''

prev_ret = np.vstack([np.zeros((1,n_paths)), ret[:-1,:]])

pos = np.ones_like(ret)
pos[prev_ret < -0.02] = 0.5

strat_ret = pos * ret

# 3. Compute final wealth and Sharpe per path

import math

# final wealth
market_final = (1 + ret).prod(axis=0)
strat_final = (1 + strat_ret).prod(axis=0)

# per-path Sharpe (daily, then annualized)
def sharpe_per_path(r, periods_per_year=252):
    mean = r.mean(axis=0)
    std = r.std(axis=0)
    daily_sharpe = np.where(std == 0, np.nan, mean / std)
    return daily_sharpe * math.sqrt(periods_per_year)

market_sharpes = sharpe_per_path(ret)
strat_sharpes = sharpe_per_path(strat_ret)

# 4. Inspect distributions

print("Market final describe:\n", pd.Series(market_final).describe())
print("Strat final describe:\n", pd.Series(strat_final).describe())

print("Market Sharpe describe:\n", pd.Series(market_sharpes).describe())
print("Strat Sharpe describe:\n", pd.Series(strat_sharpes).describe())

# Optional histograms:

import matplotlib.pyplot as plt

pd.Series(market_final).hist(bins=30, alpha=0.5, label="Market")
pd.Series(strat_final).hist(bins=30, alpha=0.5, label="Strategy")
plt.legend()
plt.title("Final Wealth Distribution")
plt.grid(True)
plt.show()

pd.Series(market_sharpes).hist(bins=30, alpha=0.5, label="Market")
pd.Series(strat_sharpes).hist(bins=30, alpha=0.5, label="Strategy")
plt.legend()
plt.title("Sharpe Distribution")
plt.grid(True)
plt.show()
