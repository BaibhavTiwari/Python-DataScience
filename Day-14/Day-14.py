import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Mean, variance, standard deviation (on returns)
np.random.seed(42)
ret = np.random.normal(loc=0.0005, scale=0.01, size=252)
s = pd.Series(ret)

mean_ret = s.mean()
var_ret = s.var(ddof=1)
std_ret = s.std(ddof=1)

print("mean:", mean_ret)
print("Variance:", var_ret)
print("Std dev", std_ret)

# 2. Sampling distribution of the mean (using Monte Carlo)

np.random.seed(42)
n_days = 252
n_paths = 1000

ret = np.random.normal(loc=0.005, scale=0.01, size=(n_days, n_paths))
sample_means = ret.mean(axis=0)

sample_means_series = pd.Series(sample_means)
print(sample_means_series.describe())

sample_means_series.hist(bins=30, figsize=(8,4))
plt.title("Distribution of sample Means (1000 paths)")
plt.xlabel("sample mean")
plt.grid(True)
plt.show()

# 3. Standard error and effect of sample size

def sample_means_for_n(n, n_paths=1000, mu=0.005, sigma=0.01):
  ret = np.random.normal(loc=mu, scale=sigma, size=(n, n_paths))
  return ret.mean(axis=0)

means_20 = sample_means_for_n(20)
means_252 = sample_means_for_n(252)

print("Std of means(20 days):", means_20.std())
print("Std of means (252 days):", means_252.std())