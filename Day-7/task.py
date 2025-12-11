import pandas as pd

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
df["Return"] = df["Close"].pct_change()
