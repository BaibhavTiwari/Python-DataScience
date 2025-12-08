import pandas as  pd

df = pd.read_csv("data.csv")
print(df.head())
print(df.info())

# read_csv loads a CSV into a DataFrame (tabular data structure of Pandas).​
# head() shows first 5 rows, info() shows columns, types, and non-null counts.​

print(df.columns)
print(df.describe())

# columns lists all column names.
# describe() gives count, mean, std, min, max, quartiles for numeric columns

df["Return"] = df["Close"].pct_change()
print(df[["Date", "Close", "Return"]].head(10))

# pct_change() computes percentage change between current and previous row (like your Day-3 returns function, but vectorized).​
# First return is NaN because there’s no previous row