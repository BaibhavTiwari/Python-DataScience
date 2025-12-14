import pandas as pd

df = pd.read_csv("data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
df["Return"] = df["Close"].pct_change()


#2. add a "DayofWeek" and do groupby

df["DayOfWeek"] = df.index.dayofweek
print(df[["Close", "Return", "DayOfWeek"]].head())

by_dow = df.groupby("DayOfWeek")["Return"].agg(["count", "mean", "std"])
print(by_dow)

'''
groupby("DayOfWeek") splits data into 7 groups.
agg(["count","mean","std"]) gives basic stats per group.
'''


#3. Group by Return_Class (if available)

'''
by_class = df.groupby("Return_Class")["Volume"].agg(["count", "mean"])
print(by_class)
'''

# 4 Correlation between numerics columns

num_cols = ["Open","High","Low","Close","Volume","Return"]
corr_matrix = df[num_cols].corr()
print(corr_matrix)

# corr() gives a correlation matrix: values between -1 and 1 measuring linear relationship between features.​

# High positive correlation (near 1) means as one goes up, the other tends to go up.

print("Corr(Close, Volume):", df["Close"].corr(df["Volume"]))
