import numpy as np
import pandas as pd
from scipy import stats

np.random.seed(42)
ret = np.random.normal(loc=0.005, scale=0.01, size=252)
s = pd.Series(ret)
n = len(s)
mean = s.mean()
std = s.std(ddof=1)
se = std/np.sqrt(n)

alpha = 0.05
df = n-1
t_crit = stats.t.ppf(1 - alpha/2, df = df)

ci_lower = mean - t_crit * se
ci_upper = mean + t_crit * se

print("Mean:", mean)
print("95% CI:", ci_lower, ci_upper)

#  2. One‑sample t‑test: is mean > 0?

t_stat, p_two_sided = stats.ttest_1samp(s, popmean=0.0)
print("t-stat:", t_stat, "p-value (two-sided):", p_two_sided)

p_one_sided = p_two_sided / 2 if t_stat > 0 else 1 - p_two_sided / 2
print("p-value (one-sided, mean > 0):", p_one_sided)

