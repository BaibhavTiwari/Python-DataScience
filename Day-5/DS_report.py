import pandas as pd

'''
Overall stats:
Mean, std, min, max of returns (from describe).

Risk-ish view:
Number of “Strong down” days vs “Strong up” days (value_counts).

Period focus:
Filter last 60 rows (df.tail(60)) and recompute Return summary for recent period.
'''

# Load CSV
df = pd.read_csv("day5.csv")

# 1. Compute Returns
df["Return"] = df["Close"].pct_change() * 100   # percentage return
df = df.dropna()  # remove first NaN return

# 2. Overall Stats
overall_stats = df["Return"].describe()[["mean", "std", "min", "max"]]
print("\n=== Overall Return Stats ===")
print(overall_stats)

# 3. Risk-ish View
# Define thresholds for strong up/down
def classify(r):
    if r >= 1:       
        return "Strong Up"
    elif r <= -1:     # –1% or lower
        return "Strong Down"
    else:
        return "Neutral"

df["Signal"] = df["Return"].apply(classify)

risk_view = df["Signal"].value_counts()
print("\n=== Strong Up vs Strong Down ===")
print(risk_view)


last_60 = df.tail(60)
recent_stats = last_60["Return"].describe()[["mean", "std", "min", "max"]]

print("\n=== Last 60 Days Return Summary ===")
print(recent_stats)
