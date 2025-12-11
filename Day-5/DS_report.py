import pandas as pd

# Load CSV
df = pd.read_csv("day5_ohlcv.csv")

# 1. Compute Returns
df["Return"] = df["Close"].pct_change() * 100
df = df.dropna()

# 2. Overall Stats
overall_stats = df["Return"].describe()[["mean", "std", "min", "max"]]
print("\n=== Overall Return Stats ===")
print(overall_stats)

# 3. Risk-ish View
def classify(r):
    if r >= 1:
        return "Strong Up"
    elif r <= -1:
        return "Strong Down"
    else:
        return "Neutral"

df["Signal"] = df["Return"].apply(classify)

risk_view = df["Signal"].value_counts()
print("\n=== Strong Up vs Strong Down ===")
print(risk_view)

# 4. Last 60 days
last_60 = df.tail(60)
recent_stats = last_60["Return"].describe()[["mean", "std", "min", "max"]]

print("\n=== Last 60 Days Return Summary ===")
print(recent_stats)
